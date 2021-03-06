# TODO: remove explicit debug settings in favor of build_ext --debug setting

import setuptools

setuptools.setup(
    name = "%",
    version = "1.0a0",
    description="Generated Python/WinRT package",
    license="MIT",
    url="http://github.com/Microsoft/xlang",
    ext_modules = [ setuptools.Extension('_%', 
        sources = [%],
        extra_compile_args = ["/std:c++17", "/await"],
        include_dirs = ['.'],
        extra_link_args=['/DEBUG'],
        libraries = ['windowsapp']) ],
    packages = setuptools.find_namespace_packages())
