import subprocess


def add_ruby_version_segment():
    try:
        version = ' %s ' % subprocess.check_output(['ruby', '-e', 'print RUBY_VERSION'], stderr=subprocess.STDOUT)
        powerline.append(version, Color.RUBY_VERSION_FG, Color.RUBY_VERSION_BG)
    except OSError:
        return

add_ruby_version_segment()
