# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:42:09 2023

@author: me123
"""

from viewer.viewer import Viewer

vi = Viewer(box_type="Kitti",bg = (255,255,255))
vi.set_ob_color_map('rainbow')
vi.add_points(points[:,0:3],
               radius = 2,
               color = (150,150,150),
               scatter_filed = points[:,2],
               alpha=1,
               del_after_show = True,
               add_to_3D_scene = True,
               add_to_2D_scene = True,
               color_map_name = "viridis")