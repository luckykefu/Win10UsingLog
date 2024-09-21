import os
import shutil


# 删除并创建符号链接
def create_symlink(src, dst):
    if os.path.exists(dst):
        if os.path.islink(dst):  # Check if it's a symbolic link
            os.remove(dst)  # Remove the symbolic link
        elif os.path.isdir(dst):
            shutil.rmtree(dst)  # Remove the directory
        else:
            os.remove(dst)  # Remove the file
    os.symlink(src, dst, target_is_directory=True)
    print(f"Symbolic link created: {dst}")

# # 创建符号链接
create_symlink(r'D:\Win\.conda', os.path.expandvars(r'%USERPROFILE%\.conda'))
create_symlink(r'D:\.ssh', os.path.expandvars(r'%USERPROFILE%\.ssh'))
create_symlink(r'D:\Documents\MySyncData\StudioOne6\FX Chains', 
               os.path.expandvars(r'%USERPROFILE%\Documents\Studio One\Presets\PreSonus\FX Chains'))

create_symlink(r'D:\Win\pip', os.path.expandvars(r'%USERPROFILE%\pip'))

# 创建 pip.ini
pip_config = """[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple/

[install]
trusted-host = pypi.mirrors.ustc.edu.cn
"""

