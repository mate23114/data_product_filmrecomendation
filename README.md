# Film Ajánló Rendszer

Ez a projekt egy film ajánló rendszer, amely a felhasználók korábbi értékelései alapján ajánl filmeket.

## Telepítés és futtatás

Kövesd az alábbi lépéseket a projekt telepítéséhez és futtatásához:

1. **Projekt klónozása**:
    ```sh
    git clone https://github.com/felhasznalo/film-ajanlo-rendszer.git
    cd film-ajanlo-rendszer
    ```

2. **Függőségek telepítése**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Adatok előkészítése**:
    ```sh
    python datas.py
    ```

4. **Modell betanítása**:
    ```sh
    python modell.py
    ```

5. **Flask szerver indítása**:
    ```sh
    python webapp.py
    ```

6. **A frontend megnyitása a böngészőben**:
    Nyisd meg a `frontend.html` fájlt a böngészőben.
