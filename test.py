from commands import labelers


for custom_labeler in labelers:
    labeler.load(custom_labeler)