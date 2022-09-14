from model import Model 
import pandas as pd
import os

def load_test_paths(base_path):
    label_dict={'Arborio':0,'basmati':1,'Ipsala':2,'Jasmine':3,'Karacadag':4}
    filenames = os.walk(base_path)
    files=list(filenames)[0][2]
    files=[file for file in files if file.endswith(".jpg")]
    labels=[label_dict[file.split(' ')[0]] for file in files]
    file_df=pd.DataFrame({"file":files,"label":labels})
    file_df["file"]=file_df.file.map(lambda x: os.path.join(base_path,x))
    return file_df
if __name__ == "__main__":
    #load data
    Test_data=load_test_paths('./Rice_Image_Dataset/Test/')
    #load model
    model=Model()
    Test_data['prediction']=Test_data.file.map(model.predict)
    accuracy=(Test_data['label']==Test_data['prediction']).sum()/Test_data.shape[0]
    print("You got {}% accuracy".format(round(accuracy*100,2)))


    
    

