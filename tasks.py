from invoke import task


@task
def demo_reset(ctx, branch="from-scratch"):
    res = ctx.run("git log main..from-scratch --oneline | tail -1 | cut -d' ' -f 1", hide=True)
    commit = res.stdout.strip()
    ctx.run(f"git checkout {commit}")


@task
def demo_next(ctx, branch="from-scratch"):
    ctx.run(f"git log --reverse --pretty=%H {branch} | grep -A 1 $(git rev-parse HEAD) | tail -n1 | xargs git checkout")

@task
def demo_prev(ctx):
    ctx.run("git checkout HEAD^1")
