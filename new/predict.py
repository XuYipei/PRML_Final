import torch
import argparse
from handout import *

def Work(test_path, checkpoint_path, preds_path):
    checkpoint = torch.load(checkpoint_path)
    lstmmodel = model.LSTMModel()
    lstmmodel.load_state_dict(checkpoint['net'])
    lstmmodel = lstmmodel.double()
    
    test_data = data.ScanFold(datapath=test_path)
    x, y = data.Format(test_data, one_hot=False, align=True)
    x = torch.tensor(x)
    y = lstmmodel.predict(x)
    
    f = open(preds_path, "w")
    f.write("smiles,activity\n")
    for i in range(y.size()[0]):
        pred = float(y[i])
        f.write(',' + str(pred) + '\n')
    f.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_path', type=str, default='./test.csv')
    parser.add_argument('--checkpoint_path', type=str, default='./checkpoint/checkpoint')
    parser.add_argument('--preds_path', type=str, default='./preds.csv')  
    arg = parser.parse_args()   

    Work(test_path=arg.test_path, checkpoint_path=arg.checkpoint_path, preds_path=arg.preds_path)