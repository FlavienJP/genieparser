expected_output =  {
    'Hu2/0/5': {
        'service_policy': {
            'output': {
                'policy_name': {
                    'llq': {
                        'class_map': {
                            'class-default': {
                                'bytes_output': 0,
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'packets': 20,
                                'queue_limit_bytes': 7500000,
                                'total_drops': 0,
                            },
                            'tc1': {
                                'match': ['traffic-class 1'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 7,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000,
                            },
                            'tc2': {
                                'match': ['traffic-class 2'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 6,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000,
                            },
                            'tc3': {
                                'match': ['traffic-class 3'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 5,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000,
                            },
                            'tc4': {
                                'match': ['traffic-class 4'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 4,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000,
                            },
                            'tc5': {
                                'match': ['traffic-class 5'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 3,
                                'shape_bc_bps': 6000000,
                                'shape_be_bps': 6000000,
                                'shape_cir_bps': 1500000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1500000000,
                            },
                            'tc6': {
                                'match': ['traffic-class 6'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 2,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000,
                            },
                            'tc7': {
                                'match': ['traffic-class 7'],
                                'match_evaluation': 'match-all',
                                'packets': 180127705,
                                'priority_level': 1,
                                'shape_bc_bps': 2000000,
                                'shape_be_bps': 2000000,
                                'shape_cir_bps': 200000000,
                                'shape_type': 'average',
                                'target_shape_rate': 200000000,
                            },
                        },
                        'queue_stats_for_all_priority_classes': {
                            'priority_level': {
                                '1': {
                                    'bytes_output': 142785841240,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 136376959112,
                                },
                                '2': {
                                    'bytes_output': 0,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 0,
                                },
                                '3': {
                                    'bytes_output': 0,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 0,
                                },
                                '4': {
                                    'bytes_output': 0,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 0,
                                },
                                '5': {
                                    'bytes_output': 0,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 0,
                                },
                                '6': {
                                    'bytes_output': 0,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 0,
                                },
                                '7': {
                                    'bytes_output': 0,
                                    'queue_limit_bytes': 96000,
                                    'queueing': True,
                                    'total_drops': 0,
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}