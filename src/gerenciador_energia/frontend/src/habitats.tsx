import { List, Datagrid, TextField, ReferenceField } from "react-admin";

export const HabitatList = () => (
    <List>
        <Datagrid>
            
            <TextField source="id" />
            <TextField source="nome" />
            
        </Datagrid>
    </List>
);
