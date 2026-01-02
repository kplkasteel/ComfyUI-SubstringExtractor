class SubstringExtractor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "begin_delimiter": ("STRING", {"default": "Begin Eyes;"}),
                "end_delimiter": ("STRING", {"default": "End Eyes;"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "extract"
    CATEGORY = "TextParsing"

    def extract(self, text, begin_delimiter, end_delimiter):
        try:
            start_index = text.find(begin_delimiter)
            if start_index == -1:
                return (f"Start delimiter not found",)
            
            start_pos = start_index + len(begin_delimiter)
            end_index = text.find(end_delimiter, start_pos)
            
            if end_index == -1:
                return (f"End delimiter not found",)
            
            return (text[start_pos:end_index].strip(),)
        except:
            return ("Error during extraction",)

NODE_CLASS_MAPPINGS = {"SubstringExtractor": SubstringExtractor}
NODE_DISPLAY_NAME_MAPPINGS = {"SubstringExtractor": "🔍 Substring Extractor"}