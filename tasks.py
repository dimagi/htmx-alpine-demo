from invoke import task


@task
def demo_reset(ctx):
    ctx.run("git log --reverse c89a46e..main --pretty=%H | head -n1 | xargs git checkout")


@task
def demo_next(ctx):
    ctx.run(f"git log --reverse --pretty=%H main | grep -A 1 $(git rev-parse HEAD) | tail -n1 | xargs git checkout")

@task
def demo_prev(ctx):
    ctx.run("git checkout HEAD^1")
