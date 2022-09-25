class AutoMultiDict(dict):
    
    def __getitem__(self, key):
        if key not in self:
            self[key] = AutoMultiDict()
        return super().__getitem__(key)

# 実行例・動作確認    
config = AutoMultiDict()
config["user"]["name"] = "Mei"
config["user"]["email"] = "sample@corp.com"
print(config)
