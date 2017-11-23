class DataMapper:
    CHUNK_SIZE = 100

    @classmethod
    def _map_chunks(cls, _list, function):
        chunks = DataMapper._chunk(_list, cls.CHUNK_SIZE)
        chunk_index = 1
        output = []

        for chunk in chunks:
            print(f"Processing chunk {chunk_index}/{len(chunks)}...")
            chunk_index += 1
            output += function(chunk)

        return output

    @staticmethod
    def _chunk(_list, chunk_size):
        return list(map(
            lambda index: _list[index:index+chunk_size],
            range(0, len(_list), chunk_size)
        ))
