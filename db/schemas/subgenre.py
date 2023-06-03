def subgenre_schema(subgenre) -> dict:
    try:
      return {
          'id': str(subgenre['id']),
          'name': subgenre['name'],
          'description': subgenre['description'],
          'linkPlaylist': subgenre['linkPlaylist'],
          'colors': subgenre['colors'],
          'bpmRange': subgenre['bpmRange'],
          'artist': subgenre['artist'],
      }
    except:
      print('error in subgendre_schema '+ subgenre['name'])

def subgenres_schema(subgenres) -> list:
    return [subgenre_schema(subgenre) for subgenre in subgenres]

