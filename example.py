import suitkit_image

search_fold = '/scratch/suit_data/level1fits/2024/06/03/normal_2k/'  # Custom Folder
filter_name = 'NB03'
add_logos=1 

#testmode
#suitkit_image.suit_co_align_fd_imgs(search_fold,filter_name,,add_logos,test_mode=True,start_idx=0,end_idx=31)
#common usage
suitkit_image.suit_co_align_fd_imgs(search_fold,filter_name,add_logos)
