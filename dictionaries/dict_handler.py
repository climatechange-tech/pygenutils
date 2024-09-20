#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-----------------------#
# Import custom modules #
#-----------------------#

from pyutils.utilities.general.introspection_utils import get_obj_type_str

#------------------#
# Define functions #
#------------------#

def sort_object_of_dictionaries(obj, sort_by="keys", custom_sort_key=None):
    
    """
    Sort a dictionary or a list/tuple/NumPy array of dictionaries by keys, values, 
    or using a custom sorting function.

    Parameters
    ----------
    obj : dict, list, tuple, or numpy.ndarray
        The dictionary or collection of dictionaries to sort.
    sort_by : str, optional
        The sorting criteria ('keys', 'values', 'custom'). Default is 'keys'.
    custom_sort_key : callable, optional
        Custom function used to sort when 'sort_by' is 'custom'.

    Returns
    -------
    sorted_obj : dict or list
        A sorted dictionary (if a single dict) or a list of sorted dictionaries.

    Raises
    ------
    TypeError
        If the input is not a dictionary, list, tuple, or NumPy array of dictionaries.
    ValueError
        If less than 2 dictionaries are provided in a list/tuple/array for sorting.
    """   
    # Input object type validation #
    #------------------------------#
    
    if get_obj_type_str(obj) not in ["dict", "list", "tuple", "ndarray"]:
        raise TypeError("Unsupported object type. "
                        "It must be dict, list, tuple or NumPy array.")
        
    if (get_obj_type_str(obj) in ["list", "tuple", "ndarray"] and len(obj)) < 2:
        raise ValueError("At least 2 dictionaries must be provided.")
        
    # Sort dictionaries #
    #-------------------#
    
    # Handle sorting by keys
    if sort_by == "keys":
        if isinstance(obj, dict):
            return {key: obj[key] for key in sorted(obj.keys())}
        return sorted(obj, key=lambda d : list(d.keys()))
        
    # Handle sorting by values
    elif sort_by == "values":
        if isinstance(obj, dict):
            return {key: obj[key] for key in sorted(obj.values())}
        return sorted(obj, key=lambda d : list(d.values()))
            
    # Handle custom sorting
    elif sort_by == "custom":
        if custom_sort_key is None:
            raise ValueError("Custom sort chosen, but no 'custom_sort_key' provided.\n")
            
        return sorted(obj, key=custom_sort_key)

def merge_dictionaries(dict_list):
    """
    Merge a list/tuple/NumPy array of dictionaries into a single dictionary.

    Parameters
    ----------
    dict_list : list, tuple, or numpy.ndarray
        A collection of dictionaries to merge.

    Returns
    -------
    merged_dict : dict
        The merged dictionary.

    Raises
    ------
    TypeError
        If the input is not a list, tuple, or NumPy array.
    ValueError
        If fewer than 2 dictionaries are provided.

    Notes
    -----
    If there are duplicate keys, the values from later dictionaries 
    will overwrite earlier ones.
    """

    # Validate the input type
    obj_type = get_obj_type_str(dict_list)
    if obj_type not in ["list", "tuple", "ndarray"]:
        raise TypeError("Unsupported object type. Must be list, tuple, or NumPy array.")
    
    if len(dict_list) < 2:
        raise ValueError("At least 2 dictionaries must be provided.")

    # Merge dictionaries
    merged_dict = {}
    for d in dict_list:
        merged_dict.update(d)
    return merged_dict

#--------------------------#
# Parameters and constants #
#--------------------------#

# Supported options #
#-------------------#

sort_by_options = ["keys", "values", "custom"]