from jinja2.sandbox import SandboxedEnvironment

# RepoGuard webhook test after changing configuration
def render_preview(
    template_source: str,
    context: dict,
) -> str:
    environment = SandboxedEnvironment()

    template = environment.from_string(
        template_source
    )

    return template.render(
        **context
    )

