---
layout: page
title: Classical Computer Vision Projects
description: Implemented Hough Transform, Bag of Visual Words, and Homography for precise scene analysis, augmented reality, and seamless image stitching
img: assets/img/sift.jpeg
# redirect: https://unsplash.com
importance: 3
category: ML AI
---

The implementation of computer vision techniques is integral to various applications, ranging from image processing to augmented reality. In a recent project, I delved into the intricate realm of computer vision and applied a multifaceted approach to image analysis and manipulation. One of the pivotal techniques employed was the Hough Transform for edge detection, a powerful method for identifying lines within an image. This technique proved instrumental in enhancing the clarity of edges, subsequently facilitating more precise scene understanding.

In the context of scene classification, I integrated the Bag of Visual Words (BoVW) model, an approach inspired by natural language processing. By extracting key visual features and representing them as a 'visual vocabulary,' the BoVW model enabled robust scene categorization. This technique proved particularly effective in discerning intricate details within images, contributing to accurate and efficient scene classification.

Augmented reality (AR) presented another exciting dimension to the project, and for accurate overlay of virtual elements onto the real-world environment, I employed Homography Estimation. This involved utilizing features such as Harris corners, coupled with descriptor matching using BRIEF and SIFT algorithms. The Harris corner detection algorithm facilitated the identification of key points in the images, while the BRIEF and SIFT descriptors provided distinctive representations for matching and aligning corresponding points. The culmination of these techniques enabled the accurate estimation of homography, essential for seamless integration of augmented reality elements into the real-world scene.

Stitching images seamlessly to create panoramic views emerged as a final aspect of the project. Leveraging the insights gained from homography estimation, I employed advanced stitching algorithms to seamlessly combine multiple images into a cohesive panorama. This process involved aligning images based on the estimated homography, correcting for distortions, and blending them seamlessly to create a visually coherent and expansive view.

In conclusion, the implementation of the Hough Transform for edge detection, Bag of Visual Words for scene classification, and Homography Estimation with features like Harris corners, BRIEF, and SIFT descriptor matching for augmented reality, showcased the synergy of diverse computer vision techniques. These methodologies, collectively harnessed, not only enhance the fundamental understanding of images but also pave the way for applications in augmented reality and panoramic imaging, demonstrating the versatility and power of computer vision in contemporary technological landscapes.
<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/hough.png"   class="img-fluid rounded z-depth-1" %}
    </div>
     <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/123.jpg"  class="img-fluid rounded z-depth-1"  %}
    </div>
</div> 
<!-- <div class="caption">
    Cleaning mechanism deisgned for the robot
</div> -->


