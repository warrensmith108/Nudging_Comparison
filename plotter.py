import numpy as np
import matplotlib.pyplot as plt
import cartopy as cp
import cartopy.crs as ccrs
import plotter_config as pc
import os
import utils
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import pickle as pkl
import glob

def draw_box(ax, left, right, bot, top, col, thk):
    ax.plot([left, left], [bot, top], color=col, linewidth=thk)
    ax.plot([right, right], [bot, top], color=col, linewidth=thk)
    ax.plot([left, right], [bot, bot], color=col, linewidth=thk)
    ax.plot([left, right], [top, top], color=col, linewidth=thk)  

def get_ACCLIP_merge_data(OBSROOT, FLT_DATES, var_str):
    
    OBSvar = []

    for FLT_DATE in FLT_DATES:
    
        AIRFILE = glob.glob(OBSROOT + '*' + FLT_DATE + '*.ict')[0]     
        AIRheaders = np.loadtxt(AIRFILE, delimiter=',', usecols = (0), dtype='str')
        AIRdata = np.loadtxt(AIRFILE, delimiter=',', skiprows=int(AIRheaders[0]))  # Read the file
        OBSvar.extend(AIRdata[:,int(list(AIRheaders).index(var_str))-11])
        
    return np.asarray(OBSvar)
    
def plot_map(ax, lon, lat, var_plot, valid_datestr, var_name, plot_lev, sim, PLOTDIR):

    # I was messing around with this but ended up just making a copy somewhere else
    # Next time you use this script and it fails, just make it work again, it won't 
    # have a negative outcome anywhere else
    
    GV_OBSROOT = '/glade/work/wsmith/ACCLIP_GV_R1_60SEC_Merge/'
    GV_FLT_DATES = ['20220819']
    ACCLIP_GV_lon = get_ACCLIP_merge_data(GV_OBSROOT, GV_FLT_DATES, 'GGLON') 
    ACCLIP_GV_lat = get_ACCLIP_merge_data(GV_OBSROOT, GV_FLT_DATES, 'GGLAT')     

    WB_OBSROOT = '/glade/work/wsmith/ACCLIP_WB57_R1_60SEC_Merge/'
    WB_FLT_DATES = ['20220819']
    ACCLIP_WB_lon = get_ACCLIP_merge_data(WB_OBSROOT, WB_FLT_DATES, 'G_LONG_MMS') 
    ACCLIP_WB_lat = get_ACCLIP_merge_data(WB_OBSROOT, WB_FLT_DATES, 'G_LAT_MMS') 
    
    lon_min = pc.lon_min
    lon_max = pc.lon_max
    lat_min = pc.lat_min
    lat_max = pc.lat_max

    ax.coastlines()
    #ax.set_title(var_name + ' at ' + str(plot_lev) + 'hPa on ' + valid_datestr)
    
    cbar_lev, cbar_rgb, norm = utils.get_colorbar(var_name, plot_lev, 0)

    cf = ax.contourf(lon, lat, var_plot, levels=cbar_lev, norm=norm, cmap=cbar_rgb, extend='both')
    #cf = ax.pcolormesh(lon, lat, var_plot, norm=norm, cmap=cbar_rgb, transform=ccrs.PlateCarree())

    #ax.scatter(ACCLIP_GV_lon, ACCLIP_GV_lat, s=0.5, color='k')
    #ax.scatter(ACCLIP_WB_lon, ACCLIP_WB_lat, s=0.5, color='k') 
    #draw_box(ax, 123, 126, 33, 38, 'magenta', 1)

    ax.set_xlim([lon_min, lon_max])
    ax.set_ylim([lat_min, lat_max])

    #plt.savefig(PLOTDIR + sim + '_' + var_name + '_' + str(plot_lev) + 'hPa_' + valid_datestr + 'Z.png')
    #plt.close('all')

    return cf

