from app.utils.template_preview import (
    render_preview,
)


def test_render_preview():
    result = render_preview(
        "Hello {{ name }}",
        {
            "name": "RepoGuard",
        },
    )

    assert result == "Hello RepoGuard-I am just testing"