from setuptools import find_packages, setup
import os

package_name = 'office_world'

def get_data_files():
    data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ]
    # Directories to include
    directories = [
        'worlds',
        'models',
        'meshes',
        'media',
        'materials',
        'launch',
        'rviz',
        'urdf',
    ]

    # Add files from each directory
    for directory in directories:
        if os.path.exists(directory):
            # Get all files in directory and subdirectories
            for dirpath, _, files in os.walk(directory):
                # Compute the install path
                install_dir = os.path.join('share', package_name, dirpath)
                # Get the full paths of files in this directory
                file_paths = [os.path.join(dirpath, f) for f in files]
                if file_paths:
                    data_files.append((install_dir, file_paths))

    return data_files


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=get_data_files(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kira',
    maintainer_email='kira@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
