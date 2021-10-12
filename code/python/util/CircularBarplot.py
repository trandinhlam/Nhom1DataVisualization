import matplotlib.pyplot as plt
import numpy as np

upperLimit = 200
lowerLimit = 50


def draw_24_hour(df):
    # initialize the figure
    plt.figure(figsize=(30, 15))
    ax = plt.subplot(111, polar=True)
    plt.axis('off')

    max = df['cases'].max()
    slope = (max - lowerLimit) / max
    heights = slope * df.cases + lowerLimit
    # Compute the width of each bar. In total we have 2*Pi = 360°
    width = 2 * np.pi / len(df.index)
    indexes = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6]
    angles = [element * width for element in indexes]
    # Draw bars
    bars = ax.bar(
        x=angles,
        height=heights,
        width=width,
        bottom=lowerLimit,
        linewidth=2,
        edgecolor="white",
        color="#61a4b2",
    )

    # little space between the bar and the label
    labelPadding = 4

    # Add labels
    for bar, angle, height, label in zip(bars, angles, heights, df["hour"]):
        # Labels are rotated. Rotation must be specified in degrees :(
        rotation = np.rad2deg(angle)
        # Flip some labels upside down
        alignment = ""
        if angle >= np.pi / 2 and angle < 3 * np.pi / 2:
            alignment = "right"
            rotation = rotation + 180
        else:
            alignment = "left"

        # Finally add the labels
        ax.text(
            x=angle,
            y=lowerLimit + bar.get_height() + labelPadding,
            s=label,
            ha=alignment,
            va='center',
            rotation=rotation,
            rotation_mode="anchor")
    plt.show()
