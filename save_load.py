#!/usr/bin/env python

import os
import joblib

def save_obj(obj, name, name_dir='data' ):  
    """
    Save to pickle.
    
    Parameters
    ----------
    obj : any object 
        This can be a dictionary or ndarray.
    name : str
        The name for the object to be saved.
    name_dir : str, default 'data'
        Name of the directory.
    
    Returns
    -------
    No return.
        Save the pickle object to the local file system.
    """

    if not os.path.isdir(name_dir):
        os.makedirs(name_dir)

    data_path = os.path.join(name_dir, name+'.pkl')
    
    with open(data_path, 'wb') as f:
        joblib.dump(obj, f)

def load_obj(name, name_dir='data' ):
    """
    Load the pickle object from the local file system.
    
    Parameters
    ----------
    obj : any object 
        This can be a dictionary or ndarray.
    name : str
        The name for the object to be saved.
    name_dir : str, default 'data'
        Name of the directory.
    
    Returns
    -------
    object
        Return an object such as a dictionary.
    """
    data_path = os.path.join(name_dir, name+'.pkl')
    
    with open(data_path, 'rb') as f:
        return joblib.load(f)