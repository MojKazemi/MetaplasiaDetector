import errno
import os
import shutil
from matplotlib.cbook import flatten
import GUI.model as len
import GUI.paths_dataset as folderPath
import GUI.create_tensor as tens
import torch
from torchvision import transforms
import kMean
import binarize
import contour 
from glob import glob
import removeColor
import cropFile

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
N_CLASSES = 1

class main():
    def __init__(self, folderPatient):

        self.folderPatient = folderPatient
        
        self.crop = cropFile.cropInpaint()
        self.quantize = kMean.Quantization()
        self.binar = binarize.GetBinariImag()
        self.cont = contour.shape()
        self.color = removeColor.shape()

        self.getpath_ = folderPath.data(folderPatient)

        self.model = len.LeNet5(N_CLASSES)
        self.model.load_state_dict(torch.load("model.pt"))

        meanBase = [0.4391, 0.3073, 0.2392]
        stdBase =  [0.2765, 0.2233, 0.1850]
        meanShape =[0.0003, 0.0003, 0.0041]
        stdShape = [0.0011, 0.0011, 0.0112]
        meanColor =[0.0207, 0.0141, 0.0130]
        stdColor = [0.0510, 0.0452, 0.0431]

        self.transfBase = transforms.Compose([transforms.Resize((32, 32)),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean = meanBase,
                                                        std  = stdBase)])
                                                        
        self.transfShape = transforms.Compose([transforms.Resize((32, 32)),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean = meanShape,
                                                        std  = stdShape)])

                                                        
        self.transfColor = transforms.Compose([transforms.Resize((32, 32)),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean = meanColor,
                                                        std  = stdColor)])



    def run(self):

        if os.path.exists(self.folderPatient + "/Results"):
            shutil.rmtree(self.folderPatient + "/Results")
        
        ORPaths = []
        for data_path in glob(self.folderPatient + "/*"):
            ORPaths.append(data_path)
        ORPaths = list(flatten(ORPaths))
        
        try: #TODO per dev 
            os.makedirs(self.folderPatient+'/Results')
            os.makedirs(self.folderPatient+'/Results/original')
            os.makedirs(self.folderPatient+'/Results/shape')
            os.makedirs(self.folderPatient+'/Results/color')
            os.makedirs(self.folderPatient+'/Results/shapeCNN')

        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        for paths_ in ORPaths: 
            self.crop.run(paths_, self.folderPatient)

        setPaths = []
        for data_path in glob(self.folderPatient+"/Results/original" + "/*"):
            setPaths.append(data_path)

        #Processing of the image 
        setPaths = list(flatten(setPaths))
        for filepath in setPaths:
            img = self.quantize.run(filepath)
            binarIMG = self.binar.main(img) #path to binar image
            self.color.run(filepath)
            self.cont.run(binarIMG, filepath) ##path to binar image, path to orginal one  
        
        self.data_path, self.shape_path, self.color_path = self.getpath_.run()

        self.dataset = tens.MakeDataset(self.data_path, transform=self.transfBase)
        self.shape_dataset = tens.MakeDataset(self.shape_path, transform=self.transfShape) 
        self.color_dataset = tens.MakeDataset(self.color_path, transform=self.transfColor) 
        probs = []
        classes_pred = []
        y_1 = torch.ones([1])
        y_0 = torch.zeros([1])
        th = 0.5
            
        for index , _ in enumerate(self.dataset):
            with torch.no_grad():
                self.model.eval()
                class_pred, prob = self.model(self.dataset[index].unsqueeze(0), self.shape_dataset[index].unsqueeze(0),self.color_dataset[index].unsqueeze(0))
                class_pred = torch.where(class_pred < th, y_0, y_1)
                probs.append(prob * 100)
                classes_pred.append(class_pred)

        return classes_pred, probs
            

if __name__ == "__main__":
    esegui = main("provaGUI")
    classes_pred, probs = esegui.run()
    print(classes_pred)
    print(probs)

