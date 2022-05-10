# Imports
import torch
from torch.utils.data import Dataset
from pathlib import Path
import numpy as np
import h5py

# Class
class H5Dataset(Dataset):
    """ HDF5 dataset loader.

    Args:
        file_path (str): Path to folder containing several or a single hdf5 file.
        data_cache_size (int): TODO
        transform (optional): Optional transform to be applied to samples.
    """

    # Constructor
    def __init__(self, file_path: str, data_cache_size=3, transform=None) -> None:
        super().__init__()

        # Constants
        self.data_info = []
        self.data_cache = {}
        self.data_cache_size = data_cache_size
        self.transform = transform

        # Find hdf5 files
        path = Path(file_path)
        if path.is_dir():
            files = sorted(path.glob('*.hdf5'))
        else:
            files = path

        # Build data structure info
        for file in files:
            self._set_info(file)

        # Debug

    # Magic methods
    def __len__(self):
        """
        Returns size of dataset
        """
        return(len(self._get_type_info('exam_id')))
    
    def __getitem__(self, index: int):
        """
        Gets items and returns as tensor
        """

        # Read data (to tensor)
        data = self.read_data('tracings', index)

        if self.transform:
            data = self.transform(data)
        else:
            data = torch.from_numpy(data)
        
        # Get label
        label = self.read_data('exam_id', index)
        label = torch.from_numpy(np.array(label))

        # Transform 
        if self.transform:
            data = 1
        # TODO
        
        # Return
        return(data, label)
    
    # Setters
    def load_data(self, file_path: str):
        """
        Loads data into cache
        """
        with h5py.File(file_path) as h5_file:
            pass

    def _set_info(self, file_path):
        # Convert path to string
        file_path = str(file_path.resolve())

        # Set info (remove 1st dimension of traces as this is scan ID)
        with h5py.File(file_path) as file:
            tracings = file['tracings']
            exam_id = file['exam_id']

            # print(tracings.shape)
            for i in range(len(tracings)):
                self.data_info.append({'file_path': file_path, 'type': 'tracings', 'shape': tracings[i,:,:].shape})
                self.data_info.append({'file_path': file_path, 'type': 'exam_id', 'shape': 1})

    # Getters
    def read_data(self, type, i):
        """
        Reads data. Will make sure data is loaded if its not already in cache.
        """
        
        # Get file path
        file_path = self._get_type_info(type)[i]['file_path']

        # Load data
        with h5py.File(file_path) as h5_file:
            if type == 'tracings':
                data = h5_file[type][i,:,:]
            elif type == 'exam_id':
                data = h5_file[type][i]
        
        return(data)

    def _get_type_info(self, type):
        """
        Extract info for a specified type of data
        """
        extracted_data = [extracted for extracted in self.data_info if extracted['type'] == type]
        return(extracted_data)
