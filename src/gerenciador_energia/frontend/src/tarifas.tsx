import { List, Datagrid, TextField } from "react-admin";

export const TarifaList = () => (
    <List>
        <Datagrid>
            
            <TextField source="id" />
            <TextField source="fonte.nome" label="Fonte" />
            <TextField source="valor_tarifa" label="Valor" />
            <TextField source="data_hora" label="Data" />
            
            
        </Datagrid>
    </List>
);
