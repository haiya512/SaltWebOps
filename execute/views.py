from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shaker.shaker_core import *
from shaker.nodegroups import *


@login_required(login_url="/account/login/")
def shell_runcmd(request):
    ng = NodeGroups()
    groups = ng.list_groups_hosts()
    # hosts =
    print groups
    return render(request,
                  'execute/minions_shell_runcmd.html',
                  {'list_groups': groups},
                  )


@login_required(login_url="/account/login/")
def shell_result(request):
    """
    如果要通过API去跑命令，就需要nodegroups.conf里面配置的是节点名，而不是主机IP
    """
    sapi = SaltAPI()
    if request.POST:
        cmd = request.POST.get("cmd").strip()
        line = "#############################################################"
        host_list = request.POST.getlist("hosts_name")
        host_str = ",".join(host_list)
        print host_str
        print cmd
        result = sapi.shell_remote_execution(host_str, cmd)
        print result
        return render(request,
                      'execute/minions_shell_result.html',
                      {'result': result, 'cmd': cmd, 'line': line}
                      )
    return render(request, 'execute/minions_shell_result.html')


@login_required(login_url="/account/login/")
def salt_runcmd(request):
    return render(request, 'execute/minions_salt_runcmd.html')
