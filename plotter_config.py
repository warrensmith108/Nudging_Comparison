# #######  This file is intended to serve as a database for information about chemical species
# #######  needed to plot them.  It also defines the cross sections that will be plotted for each

# Define the plot range here and the desired resolution of the "regridded" plot field
lat_max = 45
lat_min = 25
lon_max = 140
lon_min = 100

#lat_max = 60
#lat_min = 0
#lon_max = 180
#lon_min = 0

# Note that regridding is a time-consuming process, so there should be a balance between 
# the map size above and the resolution provided here
grid_res = 0.1  # In degrees

# Define the specs of different cross section configurations
cross_section_loc = \
    {
     '28N':[[50,28],[150,28]],   
    }

# Information for the chemical species that can be plotted
var_info = \
    {
    'CO': {
            'vars':['CO'],  # Variable arrays that should be summed to calculate the field for plotting
            'lab':'CO',     # Long name of the specie to be printed on plots
            'mod':1e9,      # Scalar modifier for the field
            'unit':'ppbv',  # Unit to be printed on the plots
            'plot_levs':[200],    # The levels that map plots should be made at
            'xlim':[0,350],
            'cross_sects':[],               # The vertical cross sections that should be made (must be defined above)
            'GV_inst':'CO_AERODYNE',
            'WB57_inst':'CO_COLD2_ppbv',
          }, 
    'XCO': {
            'vars':['XCO'],  # Variable arrays that should be summed to calculate the field for plotting
            'lab':'Column CO',     # Long name of the specie to be printed on plots
            'mod':1e9,      # Scalar modifier for the field
            'unit':'ppbv',  # Unit to be printed on the plots
            'plot_levs':[0],    # The levels that map plots should be made at
            'xlim':[0,350],
            'cross_sects':[],               # The vertical cross sections that should be made (must be defined above)
            'GV_inst':'',
            'WB57_inst':'',
          },         
    'E90': {
            'vars':['E90'],  # Variable arrays that should be summed to calculate the field for plotting
            'lab':'E90',     # Long name of the specie to be printed on plots
            'mod':1e9,      # Scalar modifier for the field
            'unit':'ppbv',  # Unit to be printed on the plots
            'plot_levs':[150],    # The levels that map plots should be made at
            'xlim':[0,350],
            'cross_sects':[],               # The vertical cross sections that should be made (must be defined above)
            'GV_inst':'',
            'WB57_inst':'',
          },         
    'SO2': {
            'vars':['SO2'],
            'lab':'SO$_2$',
            'mod':1e12,
            'unit':'pptv',   
            'xlim':[1,1000],
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'SO2_GTCIMS',
            'WB57_inst':'SO2_LIF',        
          },
    'O3': {
            'vars':['O3'],
            'lab':'O$_3$',
            'mod':1e9,
            'unit':'ppbv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[], 
            'GV_inst':'O3_ppbv',
            'WB57_inst':'O3_ppb',            
          },    
    'OH': {
            'vars':['OH'],
            'lab':'OH',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[], 
            'GV_inst':'',
            'WB57_inst':'',            
          },   
    'XOH': {
            'vars':['XOH'],
            'lab':'XOH',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[], 
            'GV_inst':'',
            'WB57_inst':'',            
          },           
    'ZMMU': {
            'vars':['ZMMU'],
            'lab':'ZM Updraft Mass Flux',
            'mod':3600,
            'unit':'kg/m2/hr',   
            'plot_levs':[250],    # The levels that map plots should be made at
            'cross_sects':[],        
          },         
    'Nudge_T': {
            'vars':['Nudge_T'],
            'lab':'T Nudging Tendency',
            'mod':3600,
            'unit':'K/hr',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },        
    'Nudge_U': {
            'vars':['Nudge_U'],
            'lab':'U Nudging Tendency',
            'mod':3600,
            'unit':'m/s/hr',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },          
    'Target_T': {
            'vars':['Target_T'],
            'lab':'Nudging Analysis T',
            'mod':1,
            'unit':'K',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },          
    'DMPDZ': {
            'vars':['DMPDZ'],
            'lab':'ZM Entrainment Rate',
            'mod':1000,
            'unit':'1000/s',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },       
    'T': {
            'vars':['T'],
            'lab':'Temperature',
            'mod':1,
            'unit':'K',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },   
    'q': {
            'vars':['Q'],
            'lab':'Specific Humidity',
            'mod':1e3,
            'unit':'g/kg',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },           
    'CMFMC_DP': {
            'vars':['CMFMC_DP'],
            'lab':'ZM Convective Mass Flux',
            'mod':3600,
            'unit':'kg/m2/hr',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },           
    'PCONVT': {
            'vars':['PCONVT'],
            'lab':'Convective Top Pressure',
            'mod':0.01,
            'unit':'hPa',   
            'plot_levs':[0],    # The levels that map plots should be made at
            'cross_sects':[],        
          },     
    'CLDHGT': {
            'vars':['CLDHGT'],
            'lab':'Cloud Height',
            'mod':1,
            'unit':'km',   
            'plot_levs':[0],    # The levels that map plots should be made at
            'cross_sects':[],        
          },        
    'DMPDZ': {
            'vars':['DMPDZ'],
            'lab':'Entrainment Rate',
            'mod':1,
            'unit':'1/s',   
            'plot_levs':[500],    # The levels that map plots should be made at
            'cross_sects':[],        
          },                
    'CAPE': {
            'vars':['CAPE'],
            'lab':'CAPE',
            'mod':1,
            'unit':'J/kg',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
          },                     
    'OCS': {
            'vars':['OCS'],  # Variable arrays that should be summed to calculate the field for plotting
            'lab':'OCS',     # Long name of the specie to be printed on plots
            'mod':1e12,      # Scalar modifier for the field
            'unit':'pptv',  # Unit to be printed on the plots
            'plot_levs':[70,100,150],    # The levels that map plots should be made at
            'cross_sects':[],               # The vertical cross sections that should be made (must be defined above)
            'GV_inst':'',
            'WB57_inst':'',            
          },   
    'DMS': {
            'vars':['DMS'],  # Variable arrays that should be summed to calculate the field for plotting
            'lab':'DMS',     # Long name of the specie to be printed on plots
            'mod':1e12,      # Scalar modifier for the field
            'unit':'pptv',  # Unit to be printed on the plots
            'plot_levs':[70,100,150],    # The levels that map plots should be made at
            'cross_sects':[],               # The vertical cross sections that should be made (must be defined above)
            'GV_inst':'',
            'WB57_inst':'',            
          },           
    'NOx': {
            'vars':['NO','NO2'],
            'lab':'NO$_x$',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },        
    'LNO_COL_PROD': {
            'vars':['LNO_COL_PROD'],
            'lab':'LNO Col Prod',
            'mod':1e3,
            'unit':'Gg/yr',   
            'plot_levs':[0],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },    
    'LNO_PROD': {
            'vars':['LNO_PROD'],
            'lab':'LNO Prod',
            'mod':1,
            'unit':'?',   
            'plot_levs':[0],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },                
    'CO_CHML': {
            'vars':['CO_CHML'],
            'lab':'CO Chem Loss',
            'mod':1,
            'unit':'molec/cm3/s',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },            
    'CO_CHMP': {
            'vars':['CO_CHMP'],
            'lab':'CO Chem Prod',
            'mod':1,
            'unit':'molec/cm3/s',   
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },         
    'CH2O': {
            'vars':['CH2O'],
            'lab':'CH$_2$O',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },        
    'C2H6': {
            'vars':['C2H6'],
            'lab':'C$_2$H$_6$',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],   
            'GV_inst':'',
            'WB57_inst':'',            
          },    
    'C3H8': {
            'vars':['C3H8'],
            'lab':'C$_3$H$_8$',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],   
            'GV_inst':'',
            'WB57_inst':'',            
          },    
    'C2H2': {
            'vars':['C2H2'],
            'lab':'C$_2$H$_2$',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },            
    'BENZENE': {
            'vars':['BENZENE'],
            'lab':'Benzene',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],  
            'GV_inst':'',
            'WB57_inst':'',            
          },
    'TOLUENE': {
            'vars':['TOLUENE'],
            'lab':'Toluene',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],  
            'GV_inst':'',
            'WB57_inst':'',            
          },        
    'CH2Cl2': {
            'vars':['CH2CL2'],
            'lab':'CH$_2$Cl$_2$',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],           
            'GV_inst':'',
            'WB57_inst':'',            
          },     
    'CH2Br2': {
            'vars':['CH2BR2'],
            'lab':'CH$_2$Br$_2$',
            'mod':1e12,
            'unit':'pptv',   
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],           
            'GV_inst':'',
            'WB57_inst':'',            
          },             
    'SO4': {
            'vars':['so4_a1','so4_a2','so4_a3'],  
            'lab':'SO$_4$',
            'mod':1013.*100.*1e9/(273.*286.9969),  # Conversion from kg/kg to ug/m3
            'xlim':[0.01,10],
            'unit':'ug m$^{-3}$',     
            'plot_levs':[150],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'sulphate_AMS',       
            'WB57_inst':'',   
    },
    'so4_a1': {
            'vars':['so4_a1'],       
            'lab':'SO$_4$',
            'GV_inst':'sulphate_AMS',
            'WB57_inst':'',
            'lims':[0,3],
            'bins':30,
            'mod':1013.*100.*1e9/(293.15*286.9969)*0.842,    # On 6-17-25, the temperature was changed to 293.15 for NTP (not STP)  # 84% of this bin mass is within the ERICA size range
            'unit':'ug m$^{-3}$ at NTP',  
            'xlim':[0.01,10],        
    },
    'so4_a2': {
            'vars':['so4_a2'],       
            'lab':'SO$_4$',
            'GV_inst':'sulphate_AMS',
            'WB57_inst':'',        
            'lims':[0,3],
            'bins':30,
            'mod':1013.*100.*1e9/(293.15*286.9969)*0.017,    # On 6-17-25, the temperature was changed to 293.15 for NTP (not STP)  # 1.7% of this bin mass is within the ERICA size range
            'unit':'ug m$^{-3}$ at NTP',   
            'xlim':[0.01,10],        
    },
    'so4_a3': {
            'vars':['so4_a3'],       
            'lab':'SO$_4$',
            'GV_inst':'sulphate_AMS',
            'WB57_inst':'',        
            'lims':[0,3],
            'bins':30,
            'mod':1013.*100.*1e9/(293.15*286.9969)*0.913,    # On 6-17-25, the temperature was changed to 293.15 for NTP (not STP)  # 91% of this bin mass is within the ERICA size range
            'unit':'ug m$^{-3}$ at NTP',    
            'xlim':[0.01,10],
          },  
    'BC': {
            'vars':['bc_a1','bc_a4'],  
            'lab':'BC',
            'mod':1013.*100.*1e9/(273.*286.9969),  # Conversion from kg/kg to ug/m3
            'unit':'ug m$^{-3}$',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },          
    'OA': {
            'vars':['soa1_a1','soa1_a2','soa2_a1','soa2_a2','soa3_a1',\
                    'soa3_a2','soa4_a1','soa4_a2','soa5_a1','soa5_a2','pom_a1','pom_a4'],  
            'lab':'OA',
            'mod':1013.*100.*1e9/(273.*286.9969),  # Conversion from kg/kg to ug/m3
            'unit':'ug m$^{-3}$',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },          
    'N2O': {
            'vars':['N2O'],  
            'lab':'N$_2$O',
            'mod':1e9,  # Conversion from kg/kg to ug/m3
            'unit':'ppbv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },     
    'CH4': {
            'vars':['CH4'],  
            'lab':'CH$_4$',
            'mod':1e6,  # Conversion from kg/kg to ug/m3
            'unit':'ppmv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },   
    'CFC11': {
            'vars':['CFC11'],  
            'lab':'CFC-11',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },   
    'CFC12': {
            'vars':['CFC12'],  
            'lab':'CFC-12',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },   
    'CFC113': {
            'vars':['CFC113'],  
            'lab':'CFC-113',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],     
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'CFC114': {
            'vars':['CFC114'],  
            'lab':'CFC-114',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],  
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'CFC115': {
            'vars':['CFC115'],  
            'lab':'CFC-115',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],     
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'HCFC22': {
            'vars':['HCFC22'],  
            'lab':'HCFC-22',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'HCFC141b': {
            'vars':['HCFC141B'],  
            'lab':'HCFC-141b',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'HCFC142b': {
            'vars':['HCFC142B'],  
            'lab':'HCFC-142b',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'CF2ClBr': {
            'vars':['CF2CLBR'],  
            'lab':'CF$_2$ClBr',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'CH3Cl': {
            'vars':['CH3CL'],  
            'lab':'CH$_3$Cl',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'CH3Br': {
            'vars':['CH3BR'],  
            'lab':'CH$_3Br',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },      
    'CH3I': {
            'vars':['CH3I'],  
            'lab':'CH$_3I',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },      
    'CHCl3': {
            'vars':['CHCL3'],  
            'lab':'CHCl$_3$',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],         
            'GV_inst':'',
            'WB57_inst':'',            
          },  
    'CH3CCl3': {
            'vars':['CH3CCL3'],  
            'lab':'CH$_3$CCl$_3$',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],     
            'GV_inst':'',
            'WB57_inst':'',            
          },          
    'CCl4': {
            'vars':['CCL4'],  
            'lab':'CCl$_4$',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },               
    'C2Cl4': {
            'vars':['C2CL4'],  
            'lab':'C$_2$Cl$_4$',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],      
            'GV_inst':'',
            'WB57_inst':'',            
          },     
    'CHBr2Cl': {
            'vars':['CHBR2CL'],  
            'lab':'CHBr$_2$Cl',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },     
    'CHBrCl2': {
            'vars':['CHBRCL2'],  
            'lab':'CHBrCl$_2$',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },             
    'CHBr3': {
            'vars':['CHBR3'],  
            'lab':'CHBr$_3$',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },     
    'ISOP': {
            'vars':['ISOP'],  
            'lab':'Isoprene',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[850],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },           
    'SFISOP': {
            'vars':['SFISOP'],  
            'lab':'Surface Isoprene',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[0],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },             
    'CF3Br': {
            'vars':['CF3BR'],  
            'lab':'CF$_3$Br',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },     
    'CH2ICl': {
            'vars':['CH2ICL'],  
            'lab':'CH$_2$ICl',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],        
            'GV_inst':'',
            'WB57_inst':'',            
          },             
    'CH3CHO': {
            'vars':['CH3CHO'],  
            'lab':'CH$_3$CHO',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],      
            'GV_inst':'',
            'WB57_inst':'',            
          }, 
    'CH3OH': {
            'vars':['CH3OH'],  
            'lab':'CH$_3$OH',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],      
            'GV_inst':'',
            'WB57_inst':'',            
          },       
    'C2H5OH': {
            'vars':['C2H5OH'],  
            'lab':'C$_2$H$_5$OH',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },      
    'HCN': {
            'vars':['HCN'],  
            'lab':'HCN',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },   
    'CH3CN': {
            'vars':['CH3CN'],  
            'lab':'CH3CN',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],          
            'GV_inst':'',
            'WB57_inst':'',            
          },           
    'MEK': {
            'vars':['MEK'],  
            'lab':'MEK',
            'mod':1e12,  # Conversion from kg/kg to ug/m3
            'unit':'pptv',     
            'plot_levs':[],    # The levels that map plots should be made at
            'cross_sects':[],       
            'GV_inst':'',
            'WB57_inst':'',            
          },                  
    }
