from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='sdf_layer',
    ext_modules=[
        CUDAExtension(
            name='sdf_layer_cuda',
            sources=['sdf_layers.cpp',
                     'sdf_matching_loss_kernel.cu'],
            include_dirs=['/usr/local/include/eigen3', '/usr/local/include', '/usr/include/eigen3', '/usr/include', '/home/hsp-user/Sophus/build/install/include', '/home/hsp-user/fmt/build/install/include'])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
