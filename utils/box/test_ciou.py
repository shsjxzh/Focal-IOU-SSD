# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

# from box_utils import match, log_sum_exp
from box_utils import match_ious, bbox_overlaps_iou, bbox_overlaps_giou, bbox_overlaps_diou, bbox_overlaps_ciou, decode

pred = torch.tensor([[9.5, 9.5, 10.5, 10.5]])
gt = torch.tensor([[9.4, 10.1, 11.6, 13.1]])

ans = bbox_overlaps_ciou(pred,gt)
print("ans: {}".format(ans))
