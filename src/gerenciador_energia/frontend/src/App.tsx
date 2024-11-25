import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { Layout } from "./Layout";
import { dataProvider } from "./dataProvider";
import { authProvider } from "./authProvider";
import { HabitatList } from "./habitats";
import { ConsumoList } from "./consumo";
import { FonteList } from "./fontes";
import { TarifaList } from "./tarifas";

export const App = () => (
  <Admin
    layout={Layout}
    dataProvider={dataProvider}
    authProvider={authProvider}
  >
    <Resource name="consumos" list={ConsumoList} />
    <Resource name="habitats" list={HabitatList} />
    <Resource name="fontes"   list={FonteList} />
    <Resource name="tarifas"  list={TarifaList} />

  </Admin>
);
