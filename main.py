import g4f
import g4f.api


if __name__ == "__main__":
    print(f'Starting server... [g4f v-{g4f.version.utils.current_version}]')
    g4f.api.run_api()
