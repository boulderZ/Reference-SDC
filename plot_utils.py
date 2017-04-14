import numpy as np
import matplotlib.pyplot as plt

def plot_subplot_images(img_array,titles=None,cmap_array=[None],transpose=0,
                    fontsize=10,figheight=12,rows = 0,wspace=.1,hspace_add=0):
    '''
    Imports:
        import numpy as np
        import matplotlib.pyplot as plt
    Description:
        Create grid of images with optional titles
        got help here:       http://stackoverflow.com/q/42475508/7447161
    Inputs:
        img_array = array of images to plot
        titles = (optional) list of titles
        rows = number of rows to plot, default assumes square matrix
        transpose = flip rows for columns,
        hspace_add = add more space for printing titles if wspace=0
    '''
    
    aspect = img_array[0].shape[0]/float(img_array[0].shape[1])
    #print( aspect)
    num_images = len(img_array)
    if transpose and rows:  # flip rows for columns
        cols = rows
        rows = int(num_images/cols)
        n = rows
        m = cols
        new_array=[]
        new_titles=[]
        for i in range(rows):
            for j in range(cols):
                new_array.append(img_array[i+j*rows])
                new_titles.append(titles[i+j*rows])
        img_array = new_array
        titles = new_titles
    elif rows:
        n = rows
        m = int(num_images/rows)
        if num_images % rows:
            print('len(img_array) = ',num_images,' not divisible by rows, truncating ...')
    else:
        grid = int(np.sqrt(num_images))  # will only show all images if square
        n = grid
        m = grid
        if num_images % grid:
            print('img_array not square, truncating ...')

    bottom = 0.1; left=0.05
    top=1.-bottom; right = 1.-left
    fisasp = (1-bottom-(1-top))/float( 1-left-(1-right) )
    #widthspace, relative to subplot size
    #wspace=0.1  # set to zero for no spacing
    hspace=wspace/float(aspect) + hspace_add #
    #fix the figure height
    #figheight= 3 # inch
    figwidth = (m + (m-1)*wspace)/float((n+(n-1)*hspace)*aspect)*figheight*fisasp

    fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(figwidth, figheight))
    plt.subplots_adjust(top=top, bottom=bottom, left=left, right=right,
                        wspace=wspace, hspace=hspace)

    im = 0
    for ax in axes.flatten():
        if len(cmap_array) == 1:
            ax.imshow(img_array[im],cmap=cmap_array[0])
        else:
            ax.imshow(img_array[im],cmap=cmap_array[im])
        if titles:
            title = titles[im]
            ax.set_title(title,fontsize=fontsize)
        ax.axis('off')
        im += 1

    plt.show()
