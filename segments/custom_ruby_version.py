import subprocess


def add_custom_ruby_version_segment():
    try:
        version = ' %s ' % " ".join(subprocess.check_output(['ruby_version'], stderr=subprocess.STDOUT, shell=True).split())
        powerline.append(version, Color.RUBY_VERSION_FG, Color.RUBY_VERSION_BG)
    except OSError as e:
        print e.errno
        print e.filename
        print e.strerror
        powerline.append("error", Color.RUBY_VERSION_FG, Color.RUBY_VERSION_BG)
        return

add_custom_ruby_version_segment()
