# -*- coding: utf-8 -*-
import re
import sys
import json

class OdbUtils():
    @staticmethod
    def initialize_data():
        """
        Initializes the temperature ranges and tool node mappings.
        """
        # Mine
        node_range_strs = {
            "h25": "900, 10860:10818:-1, 148, 6768:6755:-1, 433, 99947:100955:1, 6358",
            "h50": "880, 10850:10813:-1, 148, 6768:6755:-1, 433, 98947:99955:1, 6338",
            "h75": "860, 10840:10807:-1, 148, 6768:6755:-1, 433, 97947:98955:1, 6318",
            "h100": "840, 10830:10802:-1, 148, 6768:6755:-1, 433, 97947:97955:1, 6298"
        }
        
        # Severin
        # node_range_strs = {
        #     "h0025": "681, 16409:16381:-1, 1085, 20456:20443:-1, 1429, 79613:79605:-1, 5483",
        #     "h0050": "701, 17859:17831:-1, 1105, 21906:21893:-1, 1449, 81063:81055:-1, 5493",
        #     "h0075": "721, 19309:19281:-1, 1125, 23356:23343:-1, 1469, 82513:82505:-1, 5503",
        #     "h0100": "741, 20759:20731:-1, 1145, 24806:24793:-1, 1489, 83963:83955:-1, 5513"
        # }

        
        spanwinkel_nodes = {
            "6": 2878,  # Spanwinkel +6° → Knoten 2878
            "-6": 1795   # Spanwinkel -6° → Knoten 1795
        }
        return node_range_strs, spanwinkel_nodes

    @staticmethod
    def extract_info_from_filename(filename):
        """
            Extracts rake angle (gam) and thickness (h) from the filename.

            :param filename: Name of the ODB file
            :return: A tuple (gam, h)
        """
        gam_match = re.search(r"_gam(-?\d+)_", filename)
        h_match = re.search(r"h(\d+)", filename)
        gam = gam_match.group(1) if gam_match else None
        h = "h{}".format(h_match.group(1)) if h_match else None
        return gam, h

    @staticmethod
    def generate_node_path(node_range_str):
        """
        Generates a list of node labels based on the node range string.

        :param node_range_str: A string defining node ranges
        :return: A list of node labels
        """
        node_ranges = node_range_str.split(', ')
        node_labels = []

        for node_range in node_ranges:
            if ':' in node_range:
                # Verarbeite Knotenbereiche
                start, end, step = map(int, node_range.split(':'))
                node_labels.extend(range(start, end + step, step))  # +step, um sicherzustellen, dass der Endknoten enthalten ist
            else:
                # Verarbeite einzelne Knotenlabels
                node_labels.append(int(node_range))   
        
        return node_labels

    @staticmethod
    def calculate_distances(nodes, node_path):
        """Calculate cumulative distances between nodes along a path."""
        coords = {node.label: node.coordinates for node in nodes}
        distances = [0.0]
        for i in range(1, len(node_path)):
            dist = sum(
                (coords[node_path[i]][j] - coords[node_path[i - 1]][j]) ** 2
                for j in range(3)
            ) ** 0.5
            distances.append(distances[-1] + dist)
        return distances



