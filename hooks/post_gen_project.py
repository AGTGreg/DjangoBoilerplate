# hooks/post_gen_project.py

def main():
    use_crispy = "{{ cookiecutter.include_crispy_forms_with_bootstrap5 }}" == "y"

    if use_crispy:
        print(
            "\n✔ django-crispy-forms included. Make sure Bootstrap 5 CSS is in your base template "
            "(e.g., via CDN) so crispy’s Bootstrap components look correct."
        )

    print("{{ cookiecutter.project_name }} created! Read README.md for more information and instructions on how to get started.")


if __name__ == "__main__":
    main()
