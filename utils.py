

#################################################################
#
#  This script has a few small utillity functions to keep the main scripts cleaner
#
# ################################################################

import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

def alt2prs(alts, H, P0):
    result = P0*np.exp(-1.0*alts/H)
    return result
      
def prs2alt(prs, H, P0):
    result = -1.0*H*np.log(prs/P0)
    return result

def get_colorbar(var, plot_lev, cbar):

    cbar_dir = '/glade/u/home/wsmith/NudgeComparison_scripts/colorbars/'
    
    cbarfile = 'rgb' + str(cbar) + '.txt'
    levelfile = 'levels_' + var + '.txt'
    rgb      = np.loadtxt(cbar_dir+cbarfile, skiprows=3, usecols=(0,1,2))
    rgb_under = rgb[0,:]
    rgb_over  = rgb[-1,:]
    rgb = rgb[1:-1,:]
    rgb = rgb / 255. # normalize

    # Read in the first line of the level file to see what levels are in the file
    prslevs = np.loadtxt(cbar_dir+levelfile, max_rows=1)
    
    # Create a flag variable indicating whether there are different cbar levels for different cross sections
    if (-1 in prslevs): lev_flag = 0
    else: lev_flag = 1
    
    # Read the whole file and use the number of columns to make the output 2d
    # If this colorbar has only one set of levels for every cross section then use it.
    # Otherwise, strip out the appropriate one    
    if lev_flag == 0: 
        all_levels = np.loadtxt(cbar_dir+levelfile, skiprows=1)
        levels = all_levels
    else: 
        all_levels = np.loadtxt(cbar_dir+levelfile, skiprows=1, usecols=np.arange(len(prslevs)))
        levels = all_levels[:,list(prslevs).index(plot_lev)]
        levels = levels[levels > -900] 
    
    colormap = ListedColormap(rgb, N=len(levels)-1)
    colormap.set_under(rgb_under/255.)
    colormap.set_over(rgb_over/255.)
    norm = BoundaryNorm(levels, colormap.N)

    return levels, colormap, norm
    
def create_geo_circle(xy=(0,0), r=1):
    lat_array = []
    lon_array = []
    for angle in range(0,360):
        lat, lon = _get_location(xy=xy, angle=angle, distance=r)
        lat_array.append(lat)
        lon_array.append(lon)
    return lon_array, lat_array
    
def _get_location(xy=(0,0), angle=0, distance=1):
    x = xy[0] * np.pi / 180.
    y = xy[1] * np.pi / 180.
    angle = angle / 90 * np.pi / 2
    R = 6378.1 # radius of earth in km
    distance = distance / R

    lat = np.arcsin(np.sin(y)*np.cos(distance) + np.cos(y)*np.sin(distance)*np.cos(angle))
    lon = x + np.arctan2(np.sin(angle)*np.sin(distance)*np.cos(y), np.cos(distance) - np.sin(y)*np.sin(lat))

    lat = 180. * lat / np.pi
    lon = 180. * lon / np.pi

    return lat, lon
    
def moving_window_smooth(data, width=1):
    data_copy = np.copy(data)
    smoothed = np.zeros(data_copy.shape)
    for ix in range(data_copy.shape[0]):
        for iy in range(data_copy.shape[1]):
            smoothed[ix,iy] = np.nanmean(data_copy[ix-width:ix+width,iy-width:iy+width])
    return smoothed    
    
