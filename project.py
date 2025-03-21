# 1. นาย ณพนันท์ ศรีเกื้อกลิ่น 6706022510204 , 2. นาย ศุภกร สิริเกื้อกูลชัย 6706022510174 , 3. นาย เจตริล เจริญทอง 6706022510425
# speed eta 
# ความเร็วเฉลี่ยของแต่ละเส้นทาง

# ค่าต้นทุน ค่าน้ำมัน

#ระยะทางระหว่างอำเภอในจังหวัดปราจีนบุรี 7 อำเภอ
# 1. เมืองปราจีนบุรี
# 2. นาดี
# 3. กบินทร์บุรี
# 4. ประจันตคาม
# 5. บ้านสร้าง
# 6. ศรีมโหสถ
# 7. ศรีมหาโพธิ

# nodes_th = [
#     "เมืองปราจีนบุรี", "นาดี", "กบินทร์บุรี", "ประจันตคาม",
#     "บ้านสร้าง", "ศรีมโหสถ", "ศรีมหาโพธิ",
# ]

# nodes_road = [
#     "route 3481", "ทางหลวงชนบท ปราจีนบุรี 2033", "route 319",
#     "route 3079", "ปจ. 5026", "ทางหลวงแผ่นดินหมายเลข 3452",
#     "ทางหลวงแผ่นดินหมายเลข 3290", "ถ.กบินทร์บุรี", "route 33",
#     "โยธาธิการ", "กบินทร์บุรี - ฉะเชิงเทรา ถนน/ถนน ฉะเชิงเทรา - กบินทร์บุรี/AH19",
#     "route 3076", "ปจ.4014", "ปจ.3070", "route 3078"
# ]
#ระยะทางระหว่างอำเภอต่างๆที่เชื่อมกัน
# อำเภอเมือง ติดกับ บ้านสร้าง, ศรีมโหสถ, ศรีมหาโพธิ, ประจันตคาม   
# อำเภอเมือง ไป บ้านสร้าง
# route 3481 30.7 km
# ทางหลวงชนบท ปราจีนบุรี 2033 and route 319 and route 3481 28.8 km
# G.add_node("Alt. M.Prachin - B.Sang")
# อำเภอเมือง ไป ศรีมโหสถ
# route 319 24.8 km
# อำเภอเมือง ไป ศรีมหาโพธิ
# route 3079 30.9 km
# อำเภอเมือง ไป ประจันตคาม
# ปจ. 5026 34 km
# ทางหลวงแผ่นดินหมายเลข 3452 34.4 km
# G.add_node("Alt. M.Prachin - P.Takham")
# อำเภอนาดี ติดกับ กบินทร์บุรี ประจันตคาม
# อำเภอนาดี ไป กบินทร์บุรี
# ทางหลวงแผ่นดินหมายเลข 3290 and ถ.กบินทร์บุรี 54.5 km
# ทางหลวงแผ่นดินหมายเลข 3290 58 km
# G.add_node("Alt. N.Di - K.Buri")
# อำเภอนาดี ไป ประจันตคาม
# route 33 74.5 km
# โยธาธิการ 72 km
# G.add_node("Alt. N.Di - P.Takham")
# อำเภอกบินทร์บุรี ติดกับ นาดี ประจันตคาม ศรีมหาโพธิ
# อำเภอกบินทร์บุรี ไป นาดี
# ทางหลวงแผ่นดินหมายเลข 3290 and ถ.กบินทร์บุรี 54.5 km
# ทางหลวงแผ่นดินหมายเลข 3290 58 km
# อำเภอกบินทร์บุรี ไป ประจันตคาม
# Route 33 71.2 km
# กบินทร์บุรี - ฉะเชิงเทรา ถนน/ถนน ฉะเชิงเทรา - กบินทร์บุรี/AH19 79.2 km
# G.add_node("Alt. K.Buri - P.Takham")
# อำเภอกบินทร์บุรี ไป ศรีมหาโพธิ
# ถ. กบินทร์บุรี and กบินทร์บุรี - ฉะเชิงเทรา ถนน/ถนน ฉะเชิงเทรา - กบินทร์บุรี/AH19 38.9 km
# อำเภอประจันตคาม ติดกับ นาดี กบินทร์บุรี เมืองปราจีนบุรี ศรีมหาโพธิ
# อำเภอประจันตคาม ไป นาดี
# route 33 74.5 km
# โยธาธิการ 72 km
# อำเภอประจันตคาม ไป กบินทร์บุรี
# Route 33 71.2 km
# กบินทร์บุรี - ฉะเชิงเทรา ถนน/ถนน ฉะเชิงเทรา - กบินทร์บุรี/AH19 79.2 km
# อำเภอประจันตคาม ไป เมืองปราจีนบุรี
# ปจ. 5026 34 km
# ทางหลวงแผ่นดินหมายเลข 3452 34.4 km
# อำเภอประจันตคาม ไป ศรีมหาโพธิ
# Route 3078 45.4 km
# Route 3079 59.6 km
# G.add_node("Alt. P.Takham - S.M.Phot")
# อำเภอบ้านสร้าง ติดกับ เมืองปราจีนบุรี ศรีมโหสถ
# อำเภอบ้านสร้าง ไป เมืองปราจีนบุรี
# route 3481 30.7 km
# ทางหลวงชนบท ปราจีนบุรี 2033 and route 319 and route 3481 28.8 km
# อำเภอบ้านสร้าง ไป ศรีมโหสถ
# Route 3076 and ปจ.4014 30.1 km
# Route 319 39.2 km
# G.add_node("Alt. B.Sang - S.Mosot")
# อำเภอศรีมโหสถ ติดกับ เมืองปราจีนบุรี บ้านสร้าง ศรีมหาโพธิ
# อำเภอศรีมโหสถ ไป เมืองปราจีนบุรี
# route 319 24.8 km
# อำเภอศรีมโหสถ ไป บ้านสร้าง
# Route 3076 and ปจ.4014 30.1 km
# Route 319 39.2 km
# อำเภอศรีมโหสถ ไป ศรีมหาโพธิ
# Route 3078 21.9 km
# ปจ.3070 27.3 km
# G.add_node("Alt. S.Mosot - S.M.Phot")
# อำเภอศรีมหาโพธิ ติดกับ เมืองปราจีนบุรี กบินทร์บุรี ประจันตคาม ศรีมโหสถ
# อำเภอศรีมหาโพธิ ไป เมืองปราจีนบุรี
# route 3079 30.9 km
# อำเภอศรีมหาโพธิ ไป กบินทร์บุรี
# ถ. กบินทร์บุรี and กบินทร์บุรี - ฉะเชิงเทรา ถนน/ถนน ฉะเชิงเทรา - กบินทร์บุรี/AH19 38.9 km
# อำเภอศรีมหาโพธิ ไป ประจันตคาม
# Route 3078 45.4 km
# Route 3079 59.6 km
# อำเภอศรีมหาโพธิ ไป ศรีมโหสถ
# Route 3078 21.9 km
# ปจ.3070 27.3 km


# G.add_edge("Muang Prachinburi", "Ban Sang", weight=30.7)
# G.add_edge("Muang Prachinburi", "Alt. M.Prachin - B.Sang", weight = 28.8 / 2)
# G.add_edge("Alt. M.Prachin - B.Sang", "Ban Sang", weight = 28.8 / 2)  
# G.add_edge("Muang Prachinburi", "Si Mahosot", weight=24.8)
# G.add_edge("Muang Prachinburi", "Si Maha Phot", weight=30.9)
# G.add_edge("Muang Prachinburi", "Prachantakham", weight=34)
# G.add_edge("Muang Prachinburi", "Alt. M.Prachin - P.Takham", weight = 34.4 / 2)
# G.add_edge("Alt. M.Prachin - P.Takham", "Prachantakham", weight = 34.4 / 2)
# G.add_edge("Na Di", "Kabin Buri", weight=54.5)
# G.add_edge("Na Di", "Alt. N.Di - K.Buri", weight = 58 / 2)
# G.add_edge("Alt. N.Di - K.Buri", "Kabin Buri", weight = 58 / 2)
# G.add_edge("Na Di", "Prachantakham", weight=74.5)
# G.add_edge("Na Di", "Alt. N.Di - P.Takham", weight = 72 / 2)
# G.add_edge("Alt. N.Di - P.Takham", "Prachantakham", weight = 72 / 2)
# G.add_edge("Kabin Buri", "Prachantakham", weight=71.2)
# G.add_edge("Kabin Buri", "Alt. K.Buri - P.Takham", weight = 79.2 / 2)
# G.add_edge("Alt. K.Buri - P.Takham", "Prachantakham", weight = 79.2 / 2)
# G.add_edge("Kabin Buri", "Si Maha Phot", weight=38.9)
# G.add_edge("Prachantakham", "Si Maha Phot", weight=45.4)
# G.add_edge("Prachantakham", "Alt. P.Takham - S.M.Phot", weight = 59.6 / 2)
# G.add_edge("Alt. P.Takham - S.M.Phot", "Si Maha Phot", weight = 59.6 / 2)
# G.add_edge("Ban Sang", "Si Mahosot", weight=30.1)
# G.add_edge("Ban Sang", "Alt. B.Sang - S.Mosot", weight = 39.2 / 2)
# G.add_edge("Alt. B.Sang - S.Mosot", "Si Mahosot", weight = 39.2 / 2)
# G.add_edge("Si Mahosot", "Si Maha Phot", weight=21.9)
# G.add_edge("Si Mahosot", "Alt. S.Mosot - S.M.Phot", weight = 27.3 / 2)
# G.add_edge("Alt. S.Mosot - S.M.Phot", "Si Maha Phot", weight = 27.3 / 2)
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

G = nx.Graph()

nodes = [
    "Muang Prachinburi", "Na Di", "Kabin Buri", "Prachantakham",
    "Ban Sang", "Si Mahosot", "Si Maha Phot",
]
alternative_nodes = [
    "Alt. M.Prachin - B.Sang",
    "Alt. M.Prachin - P.Takham",
    "Alt. N.Di - K.Buri",
    "Alt. N.Di - P.Takham",
    "Alt. K.Buri - P.Takham",
    "Alt. P.Takham - S.M.Phot",
    "Alt. B.Sang - S.Mosot",
    "Alt. S.Mosot - S.M.Phot",
]

edges = [
    ("Muang Prachinburi", "Ban Sang", 30.7),
    ("Muang Prachinburi", "Si Mahosot", 24.8),
    ("Muang Prachinburi", "Si Maha Phot", 30.9),
    ("Muang Prachinburi", "Prachantakham", 34),
    ("Na Di", "Kabin Buri", 54.5),
    ("Na Di", "Prachantakham", 74.5),
    ("Kabin Buri", "Prachantakham", 71.2),
    ("Kabin Buri", "Si Maha Phot", 38.9),
    ("Prachantakham", "Si Maha Phot", 45.4),
    ("Ban Sang", "Si Mahosot", 30.1),
    ("Si Mahosot", "Si Maha Phot", 21.9),
]
edges_alternative = [
    ("Alt. M.Prachin - B.Sang", "Ban Sang", 28.8 / 2),
    ("Alt. M.Prachin - B.Sang", "Muang Prachinburi", 28.8 / 2),
    ("Alt. M.Prachin - P.Takham", "Prachantakham", 34.4 / 2),
    ("Alt. M.Prachin - P.Takham", "Muang Prachinburi", 34.4 / 2),
    ("Alt. N.Di - K.Buri", "Kabin Buri", 58 / 2),
    ("Alt. N.Di - K.Buri", "Na Di", 58 / 2),
    ("Alt. N.Di - P.Takham", "Prachantakham", 72 / 2),
    ("Alt. N.Di - P.Takham", "Na Di", 72 / 2),
    ("Alt. K.Buri - P.Takham", "Prachantakham", 79.2 / 2),
    ("Alt. K.Buri - P.Takham", "Kabin Buri", 79.2 / 2),
    ("Alt. P.Takham - S.M.Phot", "Si Maha Phot", 59.6 / 2),
    ("Alt. P.Takham - S.M.Phot", "Prachantakham", 59.6 / 2),
    ("Alt. B.Sang - S.Mosot", "Si Mahosot", 39.2 / 2),
    ("Alt. B.Sang - S.Mosot", "Ban Sang", 39.2 / 2),
    ("Alt. S.Mosot - S.M.Phot", "Si Maha Phot", 27.3 / 2),
    ("Alt. S.Mosot - S.M.Phot", "Si Mahosot", 27.3 / 2),
]

must_visit = {}

G.add_nodes_from(nodes + alternative_nodes)
G.add_weighted_edges_from(edges)
G.add_weighted_edges_from(edges_alternative)

def change_path_label(shortest_path, shortest_path_length):
    global shortest_path_label, shortest_path_length_label
    if 'shortest_path_label' in globals():
        shortest_path_label.destroy()
    if 'shortest_path_length_label' in globals():
        shortest_path_length_label.destroy()
    #if text too long it will be cut for a new line
    shortest_path_label = tk.Label(right_frame, text=f"Shortest Path: {" -> ".join(shortest_path)}")
    shortest_path_label.grid(row=0, column=0)
    shortest_path_length_label = tk.Label(right_frame, text=f"Shortest Path Length: {float(shortest_path_length):.2f} km")
    shortest_path_length_label.grid(row=1, column=0)


def find_shortest_path():
    must_visit_nodes = [node for node, var in must_visit.items() if var.get()]
    shortest_path = []
    shortest_path_length = 0
    last_visited_node = None
    if must_visit_nodes:
        for must_visit_node in must_visit_nodes:
            if last_visited_node:
                shortest_path += nx.shortest_path(G, last_visited_node, must_visit_node, weight="weight")
                shortest_path_length += nx.shortest_path_length(G, last_visited_node, must_visit_node, weight="weight")
            else:
                shortest_path += nx.shortest_path(G, combo_box_start.get(), must_visit_node, weight="weight")
                shortest_path_length += nx.shortest_path_length(G, combo_box_start.get(), must_visit_node, weight="weight")
            last_visited_node = must_visit_node
        shortest_path += nx.shortest_path(G, last_visited_node, combo_box_end.get(), weight="weight")
        shortest_path_length += nx.shortest_path_length(G, last_visited_node, combo_box_end.get(), weight="weight")

    else:
        shortest_path = nx.shortest_path(G, combo_box_start.get(), combo_box_end.get(), weight="weight")
        shortest_path_length = nx.shortest_path_length(G, combo_box_start.get(), combo_box_end.get(), weight="weight")
    shortest_path = [shortest_path[0]] + [shortest_path[i] for i in range(1, len(shortest_path)) if shortest_path[i] != shortest_path[i - 1]]
    change_path_label(shortest_path, shortest_path_length)
    edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    draw_graph(shortest_path, edges)

#draw graph
def draw_graph(shortest_path=None,edges=None):
    global canvas
    if 'canvas' in globals() and canvas is not None:
        canvas.get_tk_widget().destroy()
    fig = plt.figure(figsize=(10, 5))
    pos = nx.spring_layout(G, seed=4)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="r", width=2)
    if shortest_path:
        node_colors = ["pink" if node in shortest_path else "lightblue" for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, node_color=node_colors)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        distance_labels = {edge: f"{weight} km" for edge, weight in edge_labels.items()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=distance_labels)

    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0)

def toggle_alternative_route():
    if is_alternative_enable.get():
        G.add_nodes_from(alternative_nodes)
        G.add_weighted_edges_from(edges_alternative)
    else:
        G.remove_nodes_from(alternative_nodes)
        G.remove_edges_from(edges_alternative)

def update_checkboxes():
    global must_visit
    #clear previous checkboxes
    for widget in must_visit_frame.winfo_children():
        if isinstance(widget, tk.Checkbutton):
            widget.destroy()

    for i, node in enumerate(nodes):
        if node != combo_box_start.get() and node != combo_box_end.get():
            must_visit[node] = tk.BooleanVar(value=False)
            checkbox = tk.Checkbutton(must_visit_frame, text=node, variable=must_visit[node])
            checkbox.grid(row=0 + i, column=0)

tik = tk.Tk()

left_frame = tk.Frame(tik)
left_frame.pack(side="left", fill="y", padx=10)

right_frame = tk.Frame(tik)
right_frame.pack(side="right", fill="both", expand=True)

must_visit_frame = tk.Frame(left_frame)
must_visit_frame.grid(row=11, column=0)


tik.state("zoomed")
tik.title("Shortest Path Finder")
combo_box_start_label = tk.Label(left_frame, text="Start")
combo_box_start_label.grid(row=0, column=0)
combo_box_start = ttk.Combobox(left_frame, values=nodes, state="readonly")
combo_box_start.bind("<<ComboboxSelected>>", lambda e: update_checkboxes())
combo_box_start.grid(row=1, column=0)
combo_box_end_label = tk.Label(left_frame, text="Destination")
combo_box_end_label.grid(row=2, column=0)
combo_box_end = ttk.Combobox(left_frame, values=nodes, state="readonly")
combo_box_end.bind("<<ComboboxSelected>>", lambda e: update_checkboxes())
combo_box_end.grid(row=3, column=0)
is_alternative_enable = tk.BooleanVar(value=True)

combo_box_start.set("Muang Prachinburi")
combo_box_end.set("Si Maha Phot")
    
find_shortest_path_button = tk.Button(left_frame, text="Find Shortest Path", command=find_shortest_path)
find_shortest_path_button.grid(row=4, column=0)

#on select disable alternative route
checkbutton = tk.Checkbutton(left_frame,text="Enable Alternative Route",variable=is_alternative_enable,command=toggle_alternative_route)
checkbutton.grid(row=5, column=0)

eta_title = tk.Label(left_frame, text="Calculate Estimated Time of Arrival (ETA)")
eta_title.grid(row=6, column=0)
# Speed input box
speed_label = tk.Label(left_frame, text="Enter Speed (km/h):")
speed_label.grid(row=6, column=0)
speed_entry = tk.Entry(left_frame)
speed_entry.grid(row=7, column=0)

def calculate_eta():
    try:
        speed = float(speed_entry.get())
        if speed <= 0:
            raise ValueError("Speed must be greater than 0.")
        shortest_path = nx.shortest_path(G, combo_box_start.get(), combo_box_end.get(), weight="weight")
        shortest_path_length = nx.shortest_path_length(G, combo_box_start.get(), combo_box_end.get(), weight="weight")
        eta = shortest_path_length / speed
        minutes = eta * 60
        eta_label.config(text=f"Estimated Time of Arrival (ETA): {minutes:.2f} minutes")
    except ValueError as e:
        eta_label.config(text=f"Error: Please enter a valid speed. \n{e}")

calculate_eta_button = tk.Button(left_frame, text="Calculate ETA", command=calculate_eta)
calculate_eta_button.grid(row=8, column=0)

eta_label = tk.Label(left_frame, text="")
eta_label.grid(row=9, column=0)

required_visit_label = tk.Label(left_frame, text="Required Visit Nodes")
required_visit_label.grid(row=10, column=0)
update_checkboxes()


tik.mainloop()
