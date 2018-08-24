from visualization import runExplain,runGGradCam,runGradCam,runVanillaBP,runsmoothGrad,runGBackProp
from misc_functions import get_params
from matplotlib import pyplot as plt
# for grad cam these are the outputs:
#original_image,gray,color,result,adversarial,gray2,color2,result2

# for explain:
#original_img,heat, mask,cam,adversarialpic,heat2, cam2

# for GBP:
#original_image, colorgrads,graygrads,possal, negsal, adversarial,colorgrads2,graygrads2,possal2,negsal2

# for GGCam:
# original_image, guidedgrad, grayguidedgrad, adversarial, guidedgrad2, grayguidedgrad2

# for smooth_grad:
#original_image,colorgrads,graygrads,adversarial,colorgrads2,graygrads2

# vanilla BP:
# original_image,vanilbp,grayvanilbp,adversarial,vanilbp2,grayvanilbp2

# photo index, network, visualization
def compareAttacks(vizmethod, choose_network, image_index, training='', structure=''):
    isTrained = True
    _,_,_,img_name, = get_params(image_index,choose_network,isTrained,training, structure)
    attacks = ['FGSM','PGD','DeepFool','Boundary','SinglePixel','SalMap','LBFGS','RPGD']
    rows = 1+len(attacks)
    fig = plt.figure()
    fig.suptitle('Comparing Attacks:'+img_name+' - '+ vizmethod)


    if vizmethod == 'Explain':
        iters = 50
        j = 1
        for i in attacks:

            original_img,heat, mask,cam,\
            adversarialpic,heat2, mask2, cam2,\
                indices,orig_vals,orig_labs,adver_vals, adver_labs= runExplain(choose_network, training,isTrained,
                                                                                   structure,image_index,iters,attack_type=i)
            if j == 1:
                ax11 = fig.add_subplot(rows, 5, 1)
                ax11.imshow(original_img)
                ax11.set_title('Original Image')
                ax1 = fig.add_subplot(rows, 5, 2)
                ax1.imshow(heat)
                ax1.set_title('Learned Mask Color')
                ax2 = fig.add_subplot(rows, 5, 3)
                ax2.imshow(mask)
                ax2.set_title('Learned Mask Gray')
                ax3 = fig.add_subplot(rows, 5, 4)
                ax3.imshow(cam)
                ax3.set_title('Cam Result')
                ax9 = fig.add_subplot(rows, 5, 5)
                ax9.bar(indices, orig_vals, align='center', alpha=0.5)
                ax9.set_title('Orignial Image Predictions')
                ax9.set_xticks(indices)
                ax9.set_xticklabels(orig_labs, rotation=45, ha="right")

            ax12 = fig.add_subplot(rows, 5, 5*j+1)
            ax12.imshow(adversarialpic)
            ax12.set_title(i + ' Attack')
            ax5 = fig.add_subplot(rows, 5, 5*j+2)
            ax5.imshow(heat2)
            ax6 = fig.add_subplot(rows, 5, 5*j+3)
            ax6.imshow(mask2)
            ax6.set_title('Adversary Mask Gray')
            ax7 = fig.add_subplot(rows, 5, 5*j+4)
            ax7.imshow(cam2)
            ax7.set_title('Adversary Cam Result')
            ax10 = fig.add_subplot(rows, 5, 5*(j+1))
            ax10.bar(indices, adver_vals, align='center', alpha=0.5)
            ax10.set_title('Adversary Image Predictions')
            ax10.set_xticks(indices)
            ax10.set_xticklabels(adver_labs, rotation=45, ha="right")
            j += 1

        fig.set_size_inches(32, 81)
        fig.tight_layout()
        fig.savefig('Comparing/AttackComp' +'_' +
                    img_name +'_' +
                    vizmethod + ' (' +
                    choose_network +'_' +
                    training + '_' +
                    structure + ' )', dpi=100)



    elif vizmethod == 'GradCam':
        j=1
        for i in attacks:
            original_image,gray,color,result,adversarial,gray2,color2,result2,\
                indices,orig_vals,orig_labs,adver_vals, adver_labs = runGradCam(choose_network,training,
                                                                                       isTrained,
                                                                                       structure,image_index,
                                                                                       attack_type=i)
            if j == 1:
                ax0 = fig.add_subplot(rows,5,1)
                ax0.imshow(original_image)
                ax0.set_title('Original Image')
                ax1 = fig.add_subplot(rows,5,2)
                ax1.imshow(gray)
                ax1.set_title('Cam Grasycale')
                ax2 = fig.add_subplot(rows,5,3)
                ax2.imshow(color)
                ax2.set_title('Cam HeatMap')
                ax3 = fig.add_subplot(rows,5,4)
                ax3.imshow(result)
                ax3.set_title('Cam Result')
                ax9 = fig.add_subplot(rows,5,5)
                ax9.bar(indices,orig_vals,align='center', alpha=0.5)
                ax9.set_title('Orignial Image Predictions')
                ax9.set_xticks(indices)
                ax9.set_xticklabels(orig_labs,rotation = 45,ha="right")

            ax12 = fig.add_subplot(rows,5,5*j+1)
            ax12.imshow(adversarial)
            ax12.set_title(i + ' Attack')
            ax4 = fig.add_subplot(rows,5,5*j+2)
            ax4.imshow(gray2)
            ax4.set_title('Adversary Cam Grasycale')
            ax5 = fig.add_subplot(rows,5,5*j+3)
            ax5.imshow(color2)
            ax5.set_title('Adversary Cam HeatMap')
            ax6 = fig.add_subplot(rows,5,5*j+4)
            ax6.imshow(result2)
            ax6.set_title('Adversary Cam Result')

            ax10 = fig.add_subplot(rows,5,5*j+5)
            ax10.bar(indices,adver_vals,align='center', alpha=0.5)
            ax10.set_title('Adversary Image Predictions')
            ax10.set_xticks(indices)
            ax10.set_xticklabels(adver_labs,rotation = 45,ha="right")
            j +=1

        fig.set_size_inches(32, 81)
        fig.tight_layout()
        fig.savefig('Comparing/AttackComp' +'_' +
                    img_name +'_' +
                    vizmethod + ' (' +
                    choose_network +'_' +
                    training + '_' +
                    structure + ' )', dpi=100)

    elif vizmethod == 'GBP':
        j =1
        for i in attacks:
            original_image, colorgrads,graygrads,possal, negsal, \
            adversarial,colorgrads2,graygrads2,possal2,negsal2,\
                indices,orig_vals,orig_labs,adver_vals, adver_labs = runGBackProp(choose_network,training,
                                                                                                 isTrained,
                                                                                                 structure,image_index,
                                                                                                 attack_type=i)
            if j ==1:
                ax11 = fig.add_subplot(2,6,1)
                ax11.imshow(original_image)
                ax11.set_title('Original Image')

                ax1 = fig.add_subplot(2,6,2)
                ax1.imshow(colorgrads)
                ax1.set_title('Guided BP Color')

                ax2 = fig.add_subplot(2, 6, 3)
                ax2.imshow(graygrads)
                ax2.set_title( 'Guided BP Gray')
                ax3 = fig.add_subplot(2, 6, 4)
                ax3.imshow(possal)
                ax3.set_title('Positive Saliency')
                ax4 = fig.add_subplot(2, 6, 5)
                ax4.imshow(negsal)
                ax4.set_title('Negative Saliency')


                ax9 = fig.add_subplot(2,6,6)
                ax9.bar(indices,orig_vals,align='center', alpha=0.5)
                ax9.set_title('Orignial Image Predictions')
                ax9.set_xticks(indices)
                ax9.set_xticklabels(orig_labs,rotation = 45,ha="right")

            ax12 = fig.add_subplot(2,6,6*j+1)
            ax12.imshow(adversarial)
            ax12.set_title(i + ' Attack')
            ax5 = fig.add_subplot(2, 6, 6*j+2)
            ax5.imshow(colorgrads2)
            ax5.set_title('Adversarial Guided BP Color')
            ax6 = fig.add_subplot(2, 6, 6*j+3)
            ax6.imshow(graygrads2)
            ax6.set_title('Adversarial'+ 'Guided BP Gray')
            ax7 = fig.add_subplot(2, 6, 6*j+4)
            ax7.imshow(possal2)
            ax7.set_title('Adversarial ''Positive Saliency')
            ax8 = fig.add_subplot(2, 6, 6*j+5)
            ax8.imshow(negsal2)
            ax8.set_title('Adversarial'+'Negative Saliency')
            ax10 = fig.add_subplot(2,6,6*j+6)
            ax10.bar(indices,adver_vals,align='center', alpha=0.5)
            ax10.set_title('Adversary Image Predictions')
            ax10.set_xticks(indices)
            ax10.set_xticklabels(adver_labs,rotation = 45,ha="right")
            j += 1

        fig.set_size_inches(32, 81)
        fig.tight_layout()
        fig.savefig('Comparing/AttackComp' +'_' +
                    img_name +'_' +
                    vizmethod + ' (' +
                    choose_network +'_' +
                    training + '_' +
                    structure + ' )', dpi=100)
    elif vizmethod == 'GGradCam':
        for i in attacks:
            original_image, guidedgrad, grayguidedgrad,\
            adversarial, guidedgrad2, grayguidedgrad2,\
                indices,orig_vals,orig_labs,adver_vals, adver_labs = runGGradCam(choose_network,isTrained,training,
                                                                    structure,image_index,attack_type=i)
    elif vizmethod == 'SmoothGrad':
        j=1
        for i in attacks:
            original_image,colorgrads,graygrads,\
            adversarial,colorgrads2,graygrads2,\
                indices,orig_vals,orig_labs,adver_vals, adver_labs = runsmoothGrad(choose_network,isTrained,training,structure,
                                                               image_index,attack_type=i)
            if j ==1:
                ax0 = fig.add_subplot(rows,4,1)
                ax0.imshow(original_image)
                ax0.set_title('Original Image')

                ax1 = fig.add_subplot(rows,4,2)
                ax1.imshow(colorgrads)
                ax1.set_title('Smooth BP')
                ax2 = fig.add_subplot(rows,4, 3)
                ax2.imshow(graygrads)
                ax2.set_title('Smooth BP Gray')

                ax9 = fig.add_subplot(rows,4,4)
                ax9.bar(indices,orig_vals,align='center', alpha=0.5)
                ax9.set_title('Orignial Image Predictions')
                ax9.set_xticks(indices)
                ax9.set_xticklabels(orig_labs,rotation = 45,ha="right")

            ax12 = fig.add_subplot(rows,4,4*j+1)
            ax12.imshow(adversarial)
            ax12.set_title(i + ' Attack')
            ax3 = fig.add_subplot(rows,4,4*j+2)
            ax3.imshow(colorgrads2)
            ax3.set_title('Adversary Smooth BP')
            ax4 = fig.add_subplot(rows,4, 4*j+3)
            ax4.imshow(graygrads2)
            ax4.set_title('Adversary Smooth BP Gray')
            ax10 = fig.add_subplot(rows,4,4*j+4)
            ax10.bar(indices,adver_vals,align='center', alpha=0.5)
            ax10.set_title('Adversary Image Predictions')
            ax10.set_xticks(indices)
            ax10.set_xticklabels(adver_labs,rotation = 45,ha="right")
            j += 1

        fig.set_size_inches(32, 81)
        fig.tight_layout()
        fig.savefig('Comparing/AttackComp' +'_' +
                    img_name +'_' +
                    vizmethod + ' (' +
                    choose_network +'_' +
                    training + '_' +
                    structure + ' )', dpi=100)

    elif vizmethod == 'VanillaBP':
        j = 1
        for i in attacks:
            original_image,vanilbp,grayvanilbp,\
            adversarial,vanilbp2,grayvanilbp2,\
                indices,orig_vals,orig_labs,adver_vals, adver_labs = runVanillaBP(choose_network,isTrained,training,structure,
                                                             image_index,attack_type=i)
            if j==1:
                ax0 = fig.add_subplot(rows,4,1)
                ax0.imshow(original_image)
                ax0.set_title('Original Image')
                ax1 = fig.add_subplot(rows,4,2)
                ax1.imshow(vanilbp)
                ax1.set_title('Vanilla BackProp')
                ax2 = fig.add_subplot(rows,4,3)
                ax2.imshow(grayvanilbp)
                ax2.set_title('Vanilla BackProp GrayScale')
                ax9 = fig.add_subplot(rows,4,4)
                ax9.bar(indices,orig_vals,align='center', alpha=0.5)
                ax9.set_title('Orignial Image Predictions')
                ax9.set_xticks(indices)
                ax9.set_xticklabels(orig_labs,rotation = 45,ha="right")

            ax12 = fig.add_subplot(rows,4,j*4+1)
            ax12.imshow(adversarial)
            ax12.set_title(i + ' Attack')
            ax3 = fig.add_subplot(rows,4,j*4+2)
            ax3.imshow(vanilbp2)
            ax3.set_title('Adversary Vanilla BackProp')
            ax4 = fig.add_subplot(rows,4,j*4+3)
            ax4.imshow(grayvanilbp2)
            ax4.set_title('Adversary Vanilla BackProp GrayScale')
            ax10 = fig.add_subplot(rows,4,j*4+4)
            ax10.bar(indices,adver_vals,align='center', alpha=0.5)
            ax10.set_title('Adversary Image Predictions')
            ax10.set_xticks(indices)
            ax10.set_xticklabels(adver_labs,rotation = 45,ha="right")
            j += 1

def compareNetworks():
    print('insert code')

def compareVisualizations():
    print('insert code')

def compareTraining():
    print('insert code')