1. Task Description
Create a semi-automated system that:
Calculates which new objects can fit on a rectangular plot of land, considering existing objects and a restricted border around the edges.
Determines the available free space.
Visualizes the plot, restricted border, existing objects, and new objects that fit.
2. Functional Requirements
Write a function


python
def find_fitting_objects( plot_width: float, plot_length: float, restricted_border: float, existing_objects: list[dict], new_objects: list[dict] ) -> dict: ...
plot_width, plot_length, restricted_border: positive numbers (meters).
existing_objects: a list of dictionaries { "width": float, "length": float }.
new_objects: a list of dictionaries { "name": str, "width": float, "length": float }.
The function should:
Calculate total plot area:
total_area=plot_width×plot_lengthtotal_area=plot_width×plot_length
Calculate usable area:
usable_area=(plot_width−2×restricted_border)×(plot_length−2×restricted_border)usable_area=(plot_width−2×restricted_border)×(plot_length−2×restricted_border)
Subtract the sum of areas of existing objects (width * length) to get free_space (rounded to 2 decimals).
Select from new_objects those whose area does not exceed free_space.
If free_space < 0, return "free_space": 0.0 and an empty list.
Return dictionary:


python
{ "free_space": float, "fitting_objects": list[str] }
3. Input Validation
All numeric values must be positive.
existing_objects and new_objects must be lists containing valid dictionaries.
Raise exceptions with clear messages on invalid input.
4. Visualization
Use matplotlib to draw:

Rectangle of the plot (scaled in pixels).
Red border corresponding to restricted_border thickness.
Existing objects in blue within the border.
New fitting objects in green (no precise placement needed).
Legend identifying elements.
5. Example Usage

python
result = find_fitting_objects( plot_width=50, plot_length=100, restricted_border=4, existing_objects=[{"width":10,"length":20}, {"width":5,"length":5}], new_objects=[ {"name":"Shed","width":10,"length":10}, {"name":"Garage","width":20,"length":30}, {"name":"Cabin","width":15,"length":15} ] ) print(result) # {"free_space":4295.00, "fitting_objects":["Shed","Cabin"]}

6. Video Walkthrough (mandatory)
Record up to 30 minutes of your screen and yourself speaking, using one of these tools:
Canva Desktop ScreenRecording (free plan – 15 min; Pro – up to 2 h)
Loom (free plan – 5 min; paid – up to 30 min)
In the video:
Explain your code structure and algorithmic approach.
Demonstrate the function find_fitting_objects and matplotlib visualization.
Explain error handling and validation.
Describe how the system could be extended for precise object placement and collision avoidance.
Point out what is PoC and what you explain verbally.
Recording instructions:
Install Canva Desktop or Loom extension.
Select “Screen + Camera” or “Screen only”.
Record your presentation and copy the shareable link.
Paste the link in the submission form.
7. How To Submit
Include find_fitting_objects.py and visualization script in a repository or ZIP.
In the application form, provide:

Link to the repo or ZIP.
Link to the video recording.
Checkbox confirming GDPR consent.
Form link:
https://cedar-juniper-6b7.notion.site/292e3a7c835b81f291e5d1fc88761646?pvs=105

8. GDPR Information Clause
Following Article 13 of the GDPR, your data (including video recording) will be processed strictly for the recruitment of Python Developers at MindPal.
Legal basis: consent (Art. 6(1)(a)) and pre-contractual measures (Art. 6(1)(b)).
Data will be stored during recruitment plus 3 months after.
You have rights to access, correct, delete, restrict processing, transfer data, withdraw consent at any time, and lodge complaints with the data protection authority.
Providing data is voluntary but required for recruitment.
Data recipients: recruitment staff at MindPal and video hosting providers (Canva Inc. or Loom Inc.).
☑️ I consent to the processing of my personal data, including the video recording, for the purpose of this recruitment.
