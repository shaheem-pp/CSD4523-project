class BootstrapFormMixin:
    """Mixin to add Bootstrap 5 classes to all fields in a form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Add Bootstrap form-control class
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (
                f"{existing_classes} form-control mb-3".strip()
            )

            # Add placeholders based on input type
            if field.widget.input_type == "password":
                field.widget.attrs["placeholder"] = "Enter your password"
            elif field.widget.input_type == "email":
                field.widget.attrs["placeholder"] = "Enter your email"
            elif field.widget.input_type == "text":
                field.widget.attrs["placeholder"] = f"Enter {field.label}"
            elif field.widget.input_type == "number":
                field.widget.attrs["placeholder"] = f"Enter {field.label}"
            elif field.widget.input_type == "date":
                field.widget.attrs["placeholder"] = f"Select {field.label}"
            elif field.widget.input_type == "tel":
                field.widget.attrs["placeholder"] = f"Enter {field.label}"
            else:
                field.widget.attrs["placeholder"] = f"Enter {field.label}"

            # For select fields (dropdowns)
            if field.widget.__class__.__name__ == "Select":
                field.widget.attrs["class"] += " mb-2"
