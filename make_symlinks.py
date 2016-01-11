"""
Create symlinks for dotfiles if they don't already exist.
"""
import os

d = os.path.dirname(os.path.abspath(__file__))
home = os.path.expanduser('~')

for f in os.listdir(d):
    if f.startswith('.') and f != '.git':
        home_f = '{0}/{1}'.format(home, f)
        if not os.path.exists(home_f):
            dot_f = '{0}/{1}'.format(d, f)
            try:
                os.symlink(src=dot_f, dst=home_f)
                print('{0} => {1}'.format(dot_f, home_f))
            except Exception as e:
                print('Failed to create symlink for {0}'.format(f))
                print(e)
                raise e
