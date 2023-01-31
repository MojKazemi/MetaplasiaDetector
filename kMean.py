import cv2
from sklearn.cluster import KMeans

class Quantization(object):
    #restituisce l'immagine dopo l'applicazione dell'algoritmo kMean, appilcato su t toni di colore
    def run(self, filePath):

        sct = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

        Nr,Nc=sct.shape
        #%% Use Kmeans to perform color quantization of the image
        Ncluster=4
        kmeans = KMeans(n_clusters=Ncluster,random_state=0)# instantiate Kmeans
        A=sct.reshape(-1,1)# Ndarray, Nr*Nc rows, 1 column
        kmeans.fit(A)# run Kmeans on A
        kmeans_centroids=kmeans.cluster_centers_.flatten()#  centroids/quantized colors
        for k in range(Ncluster):
            ind=(kmeans.labels_==k)# indexes for which the label is equal to k
            A[ind]=kmeans_centroids[k]# set the quantized color
        sctq=A.reshape(Nr,Nc)# quantized image

        return sctq