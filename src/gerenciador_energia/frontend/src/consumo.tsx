import { List, Datagrid, TextField, BooleanField, useRefresh } from "react-admin";
import React, { useEffect } from 'react';


const AutoRefreshList = ({ interval, children, ...props }) => {
    const refresh = useRefresh();
    useEffect(() => {
      const intervalId = setInterval(() => {
        refresh();
      }, interval);
  
      return () => clearInterval(intervalId);
    }, [refresh, interval]);
  
    return <List {...props}>{children}</List>;
  };
  

export const ConsumoList = () => (
    <AutoRefreshList
        interval={5000}
        perPage={10}
        sort={{ field: 'data_hora', order: 'DESC' }}
    >
    <List
        perPage={10}
        sort={{ field: 'data_hora', order: 'DESC' }}
        pagination={false} // Oculta a paginação
    >
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
    </AutoRefreshList>
);
