from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class OneColumnBlock(blocks.StructBlock):
    # https://jossingram.wordpress.com/2015/08/03/parallax-background-image-block-for-wagtails-streamfield/
    background_image = ImageChooserBlock()
    col_classes = blocks.CharBlock()
    one_column = blocks.StreamBlock(
        [
            ("heading", blocks.CharBlock(classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/one_column_block.html"
