import subprocess


def add_rvm_prompt_segment():
    try:
        version = ' %s ' % " ".join(subprocess.check_output(['rvm-prompt', 'v', 'g'], stderr=subprocess.STDOUT).split())
        powerline.append(version, Color.RVM_PROMPT_FG, Color.RVM_PROMPT_BG)
    except OSError:
        return

add_rvm_prompt_segment()
