if __name__ == '__main__':
    import grasp_fusion_lib
    dataset = grasp_fusion_lib.datasets.voc.VOCClassSegmentationDataset(
        'train')
    grasp_fusion_lib.datasets.view_class_seg_dataset(dataset)
