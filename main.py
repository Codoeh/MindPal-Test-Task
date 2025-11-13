import random

from pydantic import Field, validate_call, ValidationError
from typing import Annotated
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch


def objects_validator(objects: list[dict]):
    for obj in objects:
        if "width" not in obj.keys():
            raise ValidationError("Missing width for object.")
        if "length" not in obj.keys():
            raise ValidationError("Missing length for object.")
        if obj["width"] <= 0:
            raise ValueError("Width must be positive number.")
        if obj["length"] <= 0:
            raise ValueError("Length must be positive number.")

def place_object(
        width,
        length,
        plot_width,
        plot_length,
        restricted_border)\
        :
    x = random.uniform(
        restricted_border,
        plot_width - restricted_border - width
    )
    y = random.uniform(
        restricted_border,
        plot_length - restricted_border - length
    )

    return x, y


def objects_locator(
        plot_width: Annotated[float, Field(gt=0)],
        plot_length: Annotated[float, Field(gt=0)],
        restricted_border: Annotated[float, Field(gt=0)],
        existing_objects: list[dict],
        new_objects: list[dict],
        result: dict
):

    # Create a plot
    plt.figure(figsize=(plot_width / 5, plot_length / 5))
    ax = plt.gca()
    ax.set_xlim(0, plot_width)
    ax.set_ylim(0, plot_length)
    ax.set_aspect("equal")

    # Create a land plot
    plot_rect = plt.Rectangle(
        (0, 0),
        plot_width,
        plot_length,
        edgecolor="black",
        facecolor="none",
        linewidth=2
    )
    ax.add_patch(plot_rect)

    # Existing objects
    for obj in existing_objects:
        # Chose random placement for objects
        x, y = place_object(
            width=obj["width"],
            length=obj["length"],
            plot_width=plot_width,
            plot_length=plot_length,
            restricted_border=restricted_border
        )

        # Create existing object
        existing_rect = plt.Rectangle(
            (x, y),
            width=obj["width"],
            height=obj["length"],
            edgecolor="blue",
            facecolor="none",
            linewidth=2,
        )
        ax.add_patch(existing_rect)


    # New objects
    for obj in new_objects:
        if obj["name"] in result["fitting_objects"]:
            print(obj)
            # Chose random placement for new objects
            x, y = place_object(
                width=obj["width"],
                length=obj["length"],
                plot_length=plot_length,
                plot_width=plot_width,
                restricted_border=restricted_border,
            )

            # Create new objects
            new_rect = plt.Rectangle(
                (x,y),
                width=obj["width"],
                height=obj["length"],
                edgecolor="green",
                facecolor="none",
            )
            center_x = x + obj["width"] / 2
            center_y = y + obj["length"] / 2
            ax.text(
                center_x,
                center_y,
                obj["name"],
                color="green",
                ha="center",
                va="center",
                fontsize=8
            )
            ax.add_patch(new_rect)


    # Create restricted border
    border_rect = plt.Rectangle(
        (restricted_border, restricted_border),
        plot_width - 2 * restricted_border,
        plot_length - 2 * restricted_border,
        edgecolor="red",
        facecolor="none",
        linewidth=2
    )
    ax.add_patch(border_rect)

    legend_elements = [
        Patch(facecolor="none", edgecolor="blue", label="Existing objects"),
        Patch(facecolor="none", edgecolor="green", label="Fitting new objects"),
        Patch(facecolor="none", edgecolor="red", label="Restricted border"),
    ]

    ax.legend(handles=legend_elements, loc="upper right")
    plt.show()


@validate_call
def find_fitting_objects(
        plot_width: Annotated[float, Field(gt=0)],
        plot_length: Annotated[float, Field(gt=0)],
        restricted_border: Annotated[float, Field(gt=0)],
        existing_objects: list[dict],
        new_objects: list[dict]
) -> dict:

    objects_validator(existing_objects)
    objects_validator(new_objects)

    total_area = plot_width * plot_length
    print("Total area:", total_area)

    usable_area = (plot_width - 2 * restricted_border) * (plot_length - 2 * restricted_border)
    print("Usable area:", usable_area)

    existing_objects_areas = [obj.get("length") * obj.get("width") for obj in existing_objects]
    print("Area of existing objects:", existing_objects_areas)

    free_space = round(usable_area - sum(existing_objects_areas), 2)
    print("Free space:", free_space)

    new_objects_areas = {elem.get("name"): (elem.get("width") * elem.get("length")) for elem in new_objects}
    print("Area for new objects:", new_objects_areas)

    result = {
        "free_space": free_space,
        "fitting_objects": [],
    }
    if free_space < 0:
        result["free_space"] = 0.0
        return result

    print("Result before iteration:", result)
    for key, value in new_objects_areas.items():
        if value <= result["free_space"]:
            result["free_space"] -= value
            result["fitting_objects"].append(key)
            print("Result in iteration:", result)
        else:
            continue

    objects_locator(
        plot_width=plot_width,
        plot_length=plot_length,
        restricted_border=restricted_border,
        existing_objects=existing_objects,
        new_objects=new_objects,
        result=result
    )

    return result

if __name__ == "__main__":
        find_fitting_objects(
            plot_width=50,
            plot_length=100,
            restricted_border=4,
            existing_objects=[{"width":10, "length":20}, {"width":5,"length":5}],
            new_objects=[
                {"name":"Shed","width":10,"length":10},
                {"name":"Garage","width":20,"length":30},
                {"name":"Cabin","width":15,"length":15}
            ]
        )
