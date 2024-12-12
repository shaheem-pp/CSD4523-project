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

            # Add placeholders based on input type if the widget has `input_type`
            input_type = getattr(field.widget, "input_type", None)
            if input_type == "password":
                field.widget.attrs["placeholder"] = "Enter your password"
            elif input_type == "email":
                field.widget.attrs["placeholder"] = "Enter your email"
            elif input_type in ["text", "number", "date", "tel"]:
                field.widget.attrs["placeholder"] = f"Enter {field.label}"

            # For select fields (dropdowns)
            if field.widget.__class__.__name__ == "Select":
                field.widget.attrs["class"] += " mb-2"
