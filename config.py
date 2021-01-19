# Create categorical graphical analysis - The create_categorical_charts function isolates all the object data type variables in a given data 
# frame, and generates a bar plot on the count statistics by the target variable

def create_categorical_charts(df, target_variable, vars_to_ignore):
    df = df.select_dtypes(include=['object']).copy()
    
    # Remove variables from the dataframe
    try:
        df.drop(vars_to_ignore, inplace=True, axis=1)
    except NameError:
        print('')
    except KeyError as e:
        import sys
        sys.exit(e)

    
    # Prepare the list of columns to be analyzed, and remove the target variable from the list
    categList = df.columns.to_list()
    categList.remove(target_variable)
    
    # Set the grid structure
    if len(categList)%3 != 0:
        row = (len(categList)//3) + 1
        plot=1
    else:
        row = (len(categList)//3)
        plot=1
    
    plt.figure(figsize = (15,10))
    
    # Iterate through all the plots for all categorical variables
    for i in categList:
        plt.subplot(row,3,plot)
        ax=sns.countplot(data=df,
                      x=i,
                      hue=target_variable,
                      linewidth=2,
                      palette=sns.color_palette("tab10"))
        for p in ax.patches:
            height = p.get_height()
            ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.0f}'.format(height/float(len(df)) * 100)+'%',
            ha="center") 
        plot = plot + 1
        
    plt.show()

# Create numerical graphical analysis - The create_numerical_charts function isolates all the int and float data type variables in a given  
# data frame, and generates a box plot or histogram by aggregation at the target variable

def create_numerical_charts(df, target_variable, plot_type='box', vars_to_ignore=None):
    
    target_variable = df[target_variable].to_numpy()
    no_colors = np.unique(target_variable).size
    df = df.select_dtypes(include=['float64','int64']).copy()
    
    # Remove variables from the dataframe
    try:
        while vars_to_ignore != None:
            df.drop(vars_to_ignore, inplace=True, axis=1)
    except NameError:
        print('')
    except KeyError as e:
        import sys
        sys.exit(e)

    
    # Prepare the list of columns to be analyzed, and remove the target variable from the list
    numList = df.columns.to_list()
    
    # Set the grid structure
    if len(numList)%3 != 0:
        row = (len(numList)//3) + 1
        plot=1
    else:
        row = (len(numList)//3)
        plot=1
    
    plt.figure(figsize = (15,10))
    
    # Iterate through all the plots for all categorical variables
    for i in numList:
        plt.subplot(row,3,plot)
        if plot_type == 'box':
            sns.boxplot(data=df,
                          x=target_variable,
                          y=i,
                          palette=sns.color_palette("muted"))
        elif plot_type == 'hist':
            sns.histplot(data=df,
                         hue=target_variable,
                         palette=sns.color_palette("muted", n_colors=no_colors),
                         x=i)
        else:
            print('Plot type can either be box or hist')
        plot = plot + 1
        
    plt.show()