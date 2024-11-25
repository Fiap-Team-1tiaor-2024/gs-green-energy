import { List, Datagrid, TextField, BooleanField } from "react-admin";

export const FonteList = () => (
    <List>
        <Datagrid>
            
            <TextField source="id" />
            <TextField source="nome" />
            <BooleanField source="sustentavel" />
            
            
        </Datagrid>
    </List>
);
