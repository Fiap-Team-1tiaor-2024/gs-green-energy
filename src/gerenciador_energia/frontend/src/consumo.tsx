import { List, Datagrid, TextField, BooleanField } from "react-admin";

export const ConsumoList = () => (
    <List>
        <Datagrid>
            <TextField source="id" />
            <TextField source="data_hora" />
            <TextField source="habitat.nome" label="Habitat" />
            <TextField source="tarifa.fonte.nome" label="Fonte de energia" />
            <BooleanField source="tarifa.fonte.sustentavel" label="Sustentável" />
            <TextField source="consumo_kwh" />
            <TextField source="tarifa.valor_tarifa" label="Tarifa"/>
        </Datagrid>
    </List>
);
